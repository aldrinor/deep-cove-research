# Predictive and Scheduled Autoscaling of Kubernetes Nodes: A Practitioner's Guide (October 2026)

The most effective way to scale Kubernetes nodes ahead of business demand in 2026 is not to replace the Cluster Autoscaler or Karpenter. Keep one of them as the reactive "actuator" and put a scheduled or forecast-driven "demand signal" in front of it. Until recently that signal was a deployment of negative-priority placeholder pods. It is now increasingly the standard CapacityBuffer API, which Cluster Autoscaler, Karpenter and GKE support.\[1\] Where the node pool can't grow (fixed hardware), the same signal should drive a power-management or Cluster API controller that wakes and sleeps machines you already own.

## TL;DR

- **Managed cloud (EKS/GKE/AKS):** drive capacity with a schedule or forecast (KEDA cron, Kedify/PredictKube, or your own forecaster). Have it resize a CapacityBuffer or placeholder-pod deployment, and let CA/Karpenter add nodes ahead of the peak. Add EKS warm pools or a Karpenter static NodePool (`spec.replicas`, scalable with `kubectl scale nodepool`) when you need hard node counts. Use scheduled Karpenter disruption budgets to control when scale-down is allowed.
- **Non-elastic/on-prem:** the right abstraction is "how many machines should be awake", not "how many nodes to buy". Use Cluster API MachineDeployment replicas (Metal3/OpenShift MachineAutoscaler) or an IPMI/Redfish power controller (e.g., kube-hardware-autoscaler, metalnap, both young projects). Put cordon → drain (PDB-respecting) → power-off hysteresis in front of it, and keep one or two warm standby nodes because bare-metal boot takes minutes.
- **Predictive tooling is thin and pod-centric:** Crane (last release v0.11.0, July 2023) and the Predictive HPA (v0.13.2, July 2023) are effectively dormant. AHPA is Alibaba-only, and cloud VM-level predictive scalers (EC2, GCE MIG, VMSS) are either unsupported on, or conflict with, Kubernetes-managed node groups. Build a hybrid: forecast and schedule set a floor, reactive CA/Karpenter handles the error, and asymmetric scale-down protects availability.

## Key Findings

1. **CA is reactive by design, and its defaults bias toward slow scale-down.** It acts only on unschedulable pods. Its defaults wait `scale-down-unneeded-time` = 10m, `scale-down-delay-after-add` = 10m and `scale-down-delay-after-failure` = 3m, use a 0.5 utilization threshold, and allow `max-node-provision-time` of up to 15 minutes.\[2\] In practice a node takes 10–20 minutes from "unneeded" to "deleted".\[3\]
2. **Overprovisioning is the bridge from "forecast" to "nodes".** The CA FAQ's pattern (pause pods with a low PriorityClass, optionally sized by cluster-proportional-autoscaler) is now standardized as the **CapacityBuffer** API (`autoscaling.x-k8s.io`). It is alpha in CA 1.34 and beta (v1beta1) in CA 1.35, alpha in Karpenter, and GKE previewed it as "active buffer" in April 2026.\[1\]\[4\]\[5\]\[6\]
3. **Karpenter now has first-class static capacity.** `spec.replicas` on a NodePool, scaled with `kubectl scale nodepool`, is effectively a node-count API you can drive from cron or a forecaster. Its disruption budgets support cron `schedule` + `duration` windows, which gives you time-based scale-down control.\[7\]
4. **Cloud VM-level predictive autoscalers mostly don't apply to Kubernetes node groups.** GKE says not to enable Compute Engine autoscaling on GKE-owned MIGs, and AKS doesn't support the VMSS autoscaler on node pools.\[8\]\[9\] EC2 predictive scaling can technically run on an ASG, but it writes the same desired-capacity field that CA writes.\[10\]
5. **The main failure modes reported in real implementations are operational, not statistical:** thrashing from poorly tuned models, scheduler overload from aggressive pre-scaling, and the lack of a safe rollout path (shadow → capped → full).\[11\]\[12\]\[13\]

## 1. Why the Standard Cluster Autoscaler Falls Short

**Trigger model.** CA scales up only when pods are unschedulable.\[14\] Azure's AKS docs put it plainly: "The cluster autoscaler scales up based on pending pods rather than CPU or memory pressure on nodes."\[15\] Users therefore always wait out node boot, kubelet registration, image pull and app warm-up *after* demand has already arrived.\[16\]\[17\]

**Scale-down latency (defaults, per the OVHcloud and AKS CA profile docs):**

| Parameter | Default | Effect |
|---|---|---|
| `scan-interval` | 10s | Evaluation loop |
| `scale-down-unneeded-time` | 10m | A node must be idle this long |
| `scale-down-delay-after-add` | 10m | Scale-down is paused after any scale-up |
| `scale-down-delay-after-failure` | 3m | Back-off after a failed scale-down |
| `scale-down-utilization-threshold` | 0.5 | requests/allocatable below which a node is a candidate |
| `max-graceful-termination-sec` | 600 | Pod termination wait during drain |
| `max-node-provision-time` | 15m | How long CA waits for a node |

**Non-elastic node groups.** CA only changes a node group's *desired size* between min and max. The AWS provider README says "It will only adjust the desired value".\[18\] If the node group is a fixed rack, or VMs that must be powered on rather than created, there's no cloud API for CA to call. Bare-metal providers exist only through Cluster API (see §4).

**CA features that partially help:**
- **Overprovisioning with pause pods.** From the CA FAQ: "Overprovisioning can be configured using deployment running pause pods with very low assigned priority… which keeps resources that can be used by other pods." When real pods preempt them, "pause pods become unschedulable and force CA to scale up the cluster."\[4\] Priority -10 is the cut-off. The CA FAQ says "Priority -10 will be reserved for overprovisioning pods as it is the lowest priority that triggers scaling clusters. Other pods need to use priority 0 or higher in order to be able to preempt overprovisioning pods," and AKS warns that "Nodes don't scale up if pods have a PriorityClass value below -10." The same FAQ says the "Default priority cutoff is -10 (since version 1.12, was 0 before that). It can be changed using --expendable-pods-priority-cutoff flag, but we discourage it." One team that set the flag explicitly is Delivery Hero (foodora/foodpanda), whose Medium post says it redeployed CA with "-expendable-pods-priority-cutoff=-10". Since -10 is already the default, the flag only matters on CA versions older than 1.12. The Kubernetes docs note that with Karpenter, "the replica count you set here also sets a minimum node count for your cluster."\[19\]
- **cluster-proportional-autoscaler** resizes the pause deployment as a percentage of cluster size (e.g., always 20% headroom).\[4\]
- **Parameter tuning.** AWS Prescriptive Guidance recommends `scale-down-unneeded-time: 5m`, `scale-down-delay-after-add: 5m`, `scale-down-utilization-threshold: 0.5` and the least-waste expander. It claims this can cut node count by 20–40% "without impacting workload availability".\[20\] Treat that as vendor guidance, not a measured result for your workload. On GKE, the `optimize-utilization` autoscaling profile is the managed equivalent of aggressive scale-down.\[21\]
- **Min/max manipulation.** Raising a node group's *minimum* forces CA (and the ASG/MIG/VMSS) to the new floor right away.\[22\] This is the simplest scheduled-scaling lever on all three clouds.

## 2. Scheduled (Time-Based) Node Scaling

### 2.1 Cron-driven node-pool sizing
- **AWS:** EC2 Auto Scaling scheduled actions on the ASG behind a managed or self-managed node group work best when they change **MinSize** (CA keeps control of Desired). A CronJob or EventBridge rule calling `eks update-nodegroup-config --scaling-config minSize=…` does the same thing.
- **GKE:** Cloud Scheduler → Cloud Run/Function → `gcloud container clusters update --node-pool … --min-nodes`. Do **not** use MIG autoscaling on GKE pools: GCE docs say "Do not use Compute Engine autoscaling with MIGs that are owned by Google Kubernetes Engine."\[23\]
- **AKS:** Azure Automation or a Logic App calls `az aks nodepool update --min-count/--max-count` or `az aks nodepool scale`. For full off-hours shutdown, `az aks nodepool stop/start` (Microsoft Learn, updated August 2026) has these limits: "You can't stop system pools"; "You can't stop node pools from clusters that use node auto-provisioning (NAP)"; and "Stopping the node pool also stops the Cluster Autoscaler for that node pool. Starting the node pool restarts its Cluster Autoscaler." It also warns: "Don't manually modify the number of virtual machine scale set instances in the pool while it's stopped."\[24\] The VMSS autoscaler is not supported on AKS node pools.\[8\]
- **Workload-side downscalers** shrink pods so CA/Karpenter can remove nodes. **py-kube-downscaler** (caas-team, v26.4.0, April 2026) is now maintenance-only; its successor **GoKubeDownscaler** reached GA at v1.3 and gets all new features.\[25\] **kube-green** is active (v0.7.1; the org was updated July 2026) and is listed in the CNCF Landscape, but it is *not* a CNCF Sandbox/Incubating project.\[26\]\[27\]

### 2.2 KEDA cron + overprovisioning (the canonical "nodes before the peak" recipe)
KEDA (CNCF Graduated since August 2023; latest v2.21.0, 23 September 2026) can't scale nodes itself.\[28\]\[29\] It can scale a **placeholder deployment**, which forces CA/Karpenter to add nodes. Superorbital's write-up uses exactly this: at 8:45 AM a cron ScaledObject raises the overprovisioning deployment's replicas ahead of the 9:00 peak.\[30\]

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata: { name: overprovisioning }
value: -10            # lowest value that still triggers CA scale-up
globalDefault: false
---
apiVersion: apps/v1
kind: Deployment
metadata: { name: capacity-placeholder, namespace: capacity }
spec:
  replicas: 0
  selector: { matchLabels: { app: capacity-placeholder } }
  template:
    metadata: { labels: { app: capacity-placeholder } }
    spec:
      priorityClassName: overprovisioning
      terminationGracePeriodSeconds: 0
      containers:
      - name: pause
        image: registry.k8s.io/pause:3.9
        resources: { requests: { cpu: "3", memory: 12Gi } }  # ≈ one node's allocatable
---
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata: { name: prewarm-nodes, namespace: capacity }
spec:
  scaleTargetRef: { name: capacity-placeholder }
  minReplicaCount: 0
  maxReplicaCount: 40
  triggers:
  - type: cron                      # known peak: weekdays 09:00 local
    metadata: { timezone: Europe/Berlin, start: "30 8 * * 1-5", end: "0 18 * * 1-5", desiredReplicas: "12" }
  - type: cron                      # marketing event
    metadata: { timezone: Europe/Berlin, start: "0 19 24 11 *", end: "0 23 24 11 *", desiredReplicas: "30" }
  - type: prometheus                # business-metric floor: 1 node-sized pod per 500 rps forecast
    metadata:
      serverAddress: http://prometheus:9090
      query: max_over_time(forecast_requests_per_second{svc="checkout"}[5m])
      threshold: "500"
```
KEDA takes the **max** across triggers, so the schedule acts as a floor and the metric covers the excess.\[31\] Two KEDA gotchas: scale-down policies with small percentage steps can leave the cron target stuck one replica high (kedacore/keda #5820), and `idleReplicaCount` is needed for true zero in some cron setups.\[32\]\[33\]

### 2.3 CapacityBuffer: the standardized balloon
A CapacityBuffer declares spare capacity as N "chunks" of a pod shape. The autoscaler holds them as **virtual** pending pods, so nothing is actually scheduled. Karpenter's docs say they "are never created as real Kubernetes pods" and "automatically refill when real workloads consume the pre-provisioned capacity."\[34\]
```yaml
apiVersion: autoscaling.x-k8s.io/v1beta1   # v1alpha1 on Karpenter today
kind: CapacityBuffer
metadata: { name: checkout-buffer, namespace: shop }
spec:
  provisioningStrategy: buffer.x-k8s.io/active-capacity
  scalableRef: { apiGroup: apps, kind: Deployment, name: checkout }
  percentage: 20          # buffer = 20% of current checkout replicas
  replicas: 4             # but never fewer than 4 chunks
  limits: { cpu: "64", memory: 256Gi }   # final = min(max(replicas, percentage), limits)
```
- **Status:** alpha in CA 1.34 and beta in 1.35 (the 1.35.0 release notes say "Released CapacityBuffer v1beta1 API", and buffers also respect ResourceQuotas). Alpha in Karpenter (v1.15 docs), where buffer nodes are protected from *empty* consolidation ("Node has buffer pods"). GKE preview as "active buffer", which Google says "replace[s] complex balloon pod setups".\[1\]\[34\]\[35\]\[36\]
- **Gap:** per Kedify's docs, "spec.replicas exists, but the CRD exposes no /scale subresource", so HPA/KEDA can't target the buffer directly. A /scale subresource PR (kubernetes/autoscaler #10320) is in progress. Until it lands, Kedify's ScaleAdapter (commercial) bridges cron or predictive triggers to buffer replicas, or a small controller can patch `spec.replicas`. Kedify notes that on GKE, after the buffer drops to zero, node removal "typically takes ten minutes or more."\[1\]\[37\]\[38\]

### 2.4 Karpenter: static capacity, limits and scheduled disruption
- **Static NodePools** (`spec.replicas`, docs v1.15; also in EKS Auto Mode). The controller keeps an exact node count, and you scale it with `kubectl scale nodepool <name> --replicas=N`. Constraints: a pool can't switch between static and dynamic modes; `weight` can't be set; static pools "will not be consolidated"; scale-down "will follow standard forceful disruption semantics"; `limits.nodes` caps the count during drift and replacement.\[7\]\[39\]\[40\] This is the cleanest scheduled-node primitive in any open-source autoscaler: a CronJob running `kubectl scale nodepool` is a complete scheduled node scaler. Karpenter issue #9001 records that teams currently build "Lambda + EventBridge automation" to sync replicas with future capacity reservations.\[41\]
- **Scheduled disruption budgets** control *when* scale-down may happen. "Duration and Schedule must be set together", schedules are UTC, the most restrictive active budget wins, and the default is `nodes: 10%`.\[7\]\[42\]\[43\]
```yaml
spec:
  disruption:
    consolidationPolicy: WhenEmptyOrUnderutilized   # or Balanced / WhenEmpty
    consolidateAfter: 5m
    budgets:
    - nodes: "20%"                                  # off-peak: shrink quickly
    - nodes: "0"                                    # freeze consolidation 07:30–19:30 UTC weekdays
      schedule: "30 7 * * mon-fri"
      duration: 12h
      reasons: [Underutilized]                      # still allow Empty/Drifted
```
- **No built-in predictive capacity.** Karpenter doesn't support EC2 warm pools (issue #4354 is open), and AWS's own lens says Karpenter "does not support prewarmed node pools like Auto Scaling groups".\[44\]\[45\] Use buffers, placeholder pods or static pools instead.

### 2.5 Cloud-native features (managed clusters)
- **AWS:** Since 8 April 2026, EKS **managed node groups support EC2 warm pools**. Instances can be held *Stopped* (cheaper, slower) or *Running* (faster), with optional "reuse on scale-in", and they "work with Cluster Autoscaler without requiring any additional configuration". They require On-Demand capacity with no instance weighting and don't apply to Karpenter.\[46\]\[47\] **EC2 predictive scaling** uses up to 14 days of history to produce an hourly 48-hour forecast refreshed every 6 hours, starts in forecast-only mode, offers `SchedulingBufferTime` for pre-launch, and "will not scale in" on its own. Because "the desired capacity is set to the maximum" across policies, and CA also writes Desired, combining the two on one ASG is unsupported territory.\[10\] Use forecast-only mode to *inform* a min-size schedule rather than to actuate.
- **GKE:** Cluster autoscaler plus node auto-provisioning (now preferably via ComputeClasses on 1.33.3-gke.1136000+), Autopilot, active buffers, and the `optimize-utilization` profile.\[48\] MIG **predictive autoscaling** exists but is CPU-only and must not be used on GKE MIGs.\[23\]\[49\]
- **Azure:** Microsoft's Architecture Center recommends scheduled plus metric autoscale and predictive autoscale (forecast-only first) for **VMSS workloads**, but that doesn't apply to AKS pools. For AKS, use NAP (Karpenter-based), CA profiles, min-count schedules, and nodepool stop/start.\[50\]
- **Alibaba ACK** is the only major provider with a productized predictive pod autoscaler. **AHPA** predicts demand "up to 24 hours ahead", has an `observer` mode and cron ranges, and pairs with CronHPA and "node instant scaling" for the node layer.\[51\]\[52\]\[53\]

## 3. Predictive (Forecast-Based) Scaling

### 3.1 Projects and their 2026 status

| Project | What it predicts | Node-level? | Status (Oct 2026) |
|---|---|---|---|
| **Crane** (gocrane) EHPA + TimeSeriesPrediction (DSP algorithm) | Pod metrics → HPA replicas | No (pod only; bridge via placeholders) | Last release v0.11.0, 25 Jul 2023; not archived but dormant (117 open issues) |
| **Predictive HPA** (jthomperoo, CPA framework; Holt-Winters, linear regression) | HPA replica history | No | v0.13.2, 1 Jul 2023; not archived, effectively unmaintained; community fork exists |
| **PredictKube** (Dysnix) KEDA scaler | Prometheus query, AI model via SaaS API (2 weeks of history recommended) | Via placeholder/buffer target | Still listed in KEDA (v2.6+); predictkube-libs updated May 2026; depends on closed SaaS |
| **Kedify Predictive Scaler / ScaleAdapter** | MetricPredictor forecasts → any KEDA target incl. CapacityBuffer | Yes, via buffers | Commercial, actively documented |
| **Alibaba AHPA** | RPS/CPU/GPU, up to 24h | Pods; nodes via ACK node scaling | Managed, ACK-only |
| **EC2 / GCE MIG / VMSS predictive** | VM CPU/metric | VM groups, but conflicts with K8s-managed groups | GA, but not for K8s node pools |
| **Netflix Scryer** | Historical reference: per the Netflix Technology Blog (Nov 2013), "Scryer predicts what the needs will be prior to the time of need and provisions the instances based on those predictions"; Part 2 notes "load average is a misfit for prediction because it is a result of auto scaling" | n/a | Never open-sourced; context only |

No CNCF Sandbox project dedicated to predictive *node* scaling could be verified as of this writing.

### 3.2 Research and industry evidence
- **Model choice matters less than validation.** A CNCF blog post (28 August 2026) on GPU inference describes a controller that runs every 60 seconds and forecasts 10 minutes ahead. Its lessons: deploy in **shadow mode** first; rate-limit to **20 pods per minute** because over-aggressive scaling exposed scheduler throughput limits; add a burst detector for when actual load exceeds the prediction interval; in hindsight they would roll out "shadow → capped scale… → full scale"; and "Predictive scaling keeps more nodes warm" (a cost trade-off).\[12\]\[13\]
- **Signal choice.** arXiv 2604.19705 (2026) argues that per-instance metrics are "corrupted by the scaler's own actions". It forecasts on a **cluster-wide aggregate that is invariant under scaling** (e.g., total RPS) and scales down conservatively.\[54\] Forecast business volume, not per-pod CPU.
- **Tuning risk.** The PHPA author's own Holt-Winters evaluation found pre-emptive scaling worked, but the setup also thrashed because of "poor tuning" (α=0.1, β=0.1, γ=0.9, 24h season).\[11\]
- Academic work spans ARIMA/SARIMA, Prophet, Holt-Winters, LSTM/Transformer and RL autoscalers (e.g., AAPA, arXiv 2507.05653, which uses Holt-Winters as a periodic baseline).\[55\] Almost all of it targets **pods**, not nodes.

### 3.3 Bridging pod forecasts to nodes (three patterns)
1. **Forecast → placeholder/CapacityBuffer replicas → CA/Karpenter adds nodes** (recommended; cloud-agnostic, and CA stays the safety net).
2. **Forecast → node-group floor** (ASG MinSize, GKE `--min-nodes`, AKS `--min-count`, CAPI min annotation, Karpenter static `replicas`). Simple and deterministic, but you own the bin-packing maths.
3. **Forecast → direct infrastructure API** (power on/off, MachineDeployment replicas). Needed only for non-elastic pools.

## 4. Custom Controller / Operator Patterns

### 4.1 Reference controller (kubebuilder/controller-runtime pseudo-code)
```go
// CRD: NodeCapacityPlan {target: {kind: CapacityBuffer|NodePool|MachineDeployment|PowerPool, name},
//   forecastQuery, rpsPerNode, headroomPct, leadTime, minNodes, maxNodes, scaleDown{stabilization, maxStepPct}}
func (r *Reconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    plan := getPlan(req)
    lead := plan.Spec.LeadTime  // >= p95(node provision) + p95(pod ready) + safety
    f := prom.Query(plan.Spec.ForecastQuery, at(now+lead))          // upper quantile, e.g. P90
    sched := calendar.FloorFor(now+lead)                             // business events, holidays
    observed := prom.Query("sum(rate(requests_total[2m]))")
    demandNodes := ceil(max(f, observed) * (1+plan.Spec.HeadroomPct) / plan.Spec.RpsPerNode)
    desired := clamp(max(demandNodes, sched), plan.Spec.MinNodes, plan.Spec.MaxNodes)
    cur := target.Current()
    if desired > cur { target.Set(desired) }                         // scale up immediately
    else if stableBelow(desired, plan.Spec.ScaleDown.Stabilization) {// hysteresis
        target.Set(max(desired, cur - step(cur, plan.Spec.ScaleDown.MaxStepPct)))
    }
    emitMetrics(f, observed, desired, cur)                           // for backtesting
    return ctrl.Result{RequeueAfter: time.Minute}, nil
}
```
Actuators: CapacityBuffer `spec.replicas`, Karpenter `kubectl scale nodepool`, a CAPI MachineDeployment `scale` subresource, or a cloud API (ASG/MIG/VMSS min). Metacontroller or Operator SDK work equally well for the reconcile loop.

### 4.2 Cluster API (on-prem, private cloud, bare metal)
- CA's `clusterapi` provider scales MachineSets, MachineDeployments and MachinePools that carry `cluster.x-k8s.io/cluster-api-autoscaler-node-group-min-size` / `max-size` annotations. Scale-from-zero needs `capacity.cluster-autoscaler.kubernetes.io/*` annotations unless the infrastructure provider publishes capacity.\[56\]\[57\]
- **Scheduled floors on CAPI** = patch the min-size annotation from a CronJob, or GitOps-commit `replicas` for non-autoscaled pools (Flux pattern). Note that Syself reports "Cluster API rejects a pool that has replicas and the autoscaler min/max annotations at the same time", so choose one owner per pool.\[58\]\[59\]
- **OpenShift** uses ClusterAutoscaler + MachineAutoscaler on bare-metal MachineSets (Red Hat documents this with Metal3).\[60\] Karpenter also has an **alpha** Cluster API provider. One 2026 analysis (bex.co) argues it doesn't yet do consolidation and that Metal3/Tinkerbell provisioning "run[s] for minutes per node".\[57\] That is secondary analysis, but it matches the physics of PXE-and-image workflows.

### 4.3 Truly non-elastic pools: power management
- **kube-hardware-autoscaler** (safewords) is an operator that "powers bare-metal nodes on and off based on demand" via IPMI, Redfish, PiKVM/NanoKVM/JetKVM or Wake-on-LAN. It bin-packs unschedulable pods onto powered-off machines and drains through the eviction API, "which respects PDBs", with a dry-run mode.\[61\]
- **metalnap** "watches a demand signal, works out how many machines should be awake" and powers nodes over IPMI, Redfish, WoL or a PDU, with off/dry_run/on modes. Its warning is critical: it "must not be scheduled onto a node it manages, or it will cordon and power off the machine it is running on."\[62\] Recent PRs handle "wedged" nodes that don't come back Ready.\[63\]
- Both are young, small projects whose maturity and adoption couldn't be verified. Treat them as reference designs and run them in dry-run first. The underlying CA feature request for IPMI autoscaling (kubernetes/autoscaler #1060) was never implemented upstream.\[64\]
- **VM elasticity on fixed hardware:** run worker VMs on KubeVirt, Harvester, Proxmox or vSphere and scale them with the matching CAPI provider. This turns a fixed rack into an "elastic" pool bounded by host capacity, at the price of a virtualization layer.

**Safe power-off workflow:** cordon → evict (PDB-respecting, bounded timeout) → wait for DaemonSet-only → mark node with a "sleeping" taint/label → BMC soft-off → silence node alerts (metalnap mutes only the nodes it put down).\[63\]\[65\]\[66\] Wake-up is the reverse. Keep the node object so scheduling simulation still knows the capacity exists.

## 5. Scale-Down: Prompt but Safe

- **Asymmetric policy:** scale up on the max of forecast, schedule and observed; scale down only after a stabilization window, in bounded steps (e.g., ≤10–20% of nodes per interval, which mirrors Karpenter's default 10% budget).
- **PDBs everywhere** for replicated services. Karpenter's `terminationGracePeriod` bounds how long PDBs and `do-not-disrupt` can block a drain.\[7\] CA's `max-graceful-termination-sec` defaults to 600s.\[67\]
- **Time-box disruption:** use scheduled Karpenter budgets (`nodes: "0"` during business hours) and allow aggressive consolidation off-peak.\[68\] With CA, raise min-size during peak windows so scale-down can't undercut the floor.
- **DaemonSets and local storage:** CA can be blocked by pods with local storage or kube-system pods (`skip-nodes-with-local-storage`, `skip-nodes-with-system-pods`).\[69\] Audit these, or nodes will never drain.
- **Spot/preemptible:** keep forecast-driven *baseline* capacity on on-demand or reserved instances, and let spot absorb the reactive excess. Karpenter prioritizes reserved → spot → on-demand.\[7\]
- **Warm pools with reuse-on-scale-in** (EKS MNG) make scale-down cheap to reverse.\[47\] Stopped instances keep you paying for volumes but not compute.

## 6. Metrics and Forecasting Pipeline

1. **Ingest** business volume rather than CPU: ingress/API-gateway RPS, Kafka lag, queue depth, checkout counts (Prometheus/OTel). Keep at least 2 weeks of history. The AWS EC2 Auto Scaling User Guide says a metric "must have at least 24 hours of data" before forecasting starts, that it analyzes "up to the past 14 days", and that "The forecast is updated every 6 hours"; the GetPredictiveScalingForecast API reference adds that "having a full 14 days of historical data results in more accurate forecasts." PredictKube recommends 7–14 days.
2. **Forecast** at 1–5 minute granularity with daily and weekly seasonality plus a holiday/event calendar (Prophet, SARIMA or Holt-Winters are enough for most traffic; use LSTMs only if backtests justify them). Predict an **upper quantile**, not the mean.
3. **Lead time ≥ node provision + image pull + pod readiness + one control-loop interval.** Measure p95 of each. Cloud VMs usually take minutes, and bare-metal PXE takes minutes per node. EC2's `SchedulingBufferTime` and KEDA cron start times should encode this lead.\[10\]\[70\]
4. **Convert** RPS → pods (from load tests) → nodes (bin-packing on allocatable, not raw capacity) + headroom %.
5. **Hybrid fallback:** forecast and schedule set the floor, and reactive HPA/KEDA plus CA/Karpenter cover forecast error. Take the max, never the replacement.
6. **Observe and backtest:** record forecast vs. actual (MAPE, under-forecast minutes), pending-pod seconds, buffer fill rate, and node-hours wasted. Run in shadow mode until under-forecast risk is acceptable, as AWS's forecast-only mode and the CNCF team's shadow phase both did.\[10\]\[12\]

## 7. Comparison Matrix

| Approach | Complexity | Lead time | Cost efficiency | Cloud dependence | Non-elastic fit | Maturity |
|---|---|---|---|---|---|---|
| CA parameter tuning | Low | None (reactive) | Medium | Any CA provider | Poor | GA |
| Static pause-pod overprovisioning (+CPA) | Low | Instant within buffer | Low (24/7 headroom) | None | Only if pool can grow | Mature pattern |
| KEDA cron → placeholder pods | Low–Med | Schedule-defined | High for regular peaks | None | Only with CAPI/power actuator | KEDA GA/Graduated |
| CapacityBuffer (CA/Karpenter/GKE) | Low | Instant within buffer | Med–High (resizable) | None (API is OSS) | Same as above | Beta (CA), alpha (Karpenter), preview (GKE) |
| Cron → node-group min (ASG/MIG/VMSS/CAPI) | Low | Schedule-defined | High | Cloud API or CAPI | Good with CAPI | Mature |
| Karpenter static NodePool + `kubectl scale` | Low | Schedule/forecast-defined | High | Karpenter providers | n/a | GA feature in v1.x docs |
| EKS warm pools | Low | Cuts boot time | Medium | AWS MNG + CA only | n/a | GA (Apr 2026) |
| EC2/MIG/VMSS predictive | Low | Up to 48h | High | Cloud-specific | n/a | GA, **unsupported/conflicting on K8s pools** |
| Pod predictive (Crane, PHPA, PredictKube, AHPA) + buffers | Med–High | Forecast horizon | High if accurate | AHPA: Alibaba; PredictKube: SaaS | Via actuator | Crane/PHPA dormant; AHPA managed |
| Custom forecast operator | High | Configurable | Highest | Your choice | Excellent | You own it |
| Power-management operator (IPMI/Redfish/WoL) | Med–High | Minutes (boot) | High (energy) | None | **Best** | Young projects |

## 8. Recommended Reference Architectures

**(a) Managed cloud, elastic node groups**
- **EKS:** Karpenter, with a dynamic NodePool for burst plus a **static NodePool** for the forecast floor (a CronJob or forecaster runs `kubectl scale nodepool`), or a CapacityBuffer whose replicas a controller sets from the forecast. Use scheduled disruption budgets to freeze consolidation during peaks. If you're on CA with managed node groups, add **warm pools** and cron MinSize changes.
- **GKE:** CA + ComputeClasses/NAP + **active buffer**, with the buffer sized by schedule or forecast (Kedify ScaleAdapter or your own patcher). Cloud Scheduler sets `--min-nodes` for big known events. Use the `optimize-utilization` profile for trough scale-down.
- **AKS:** CA (or NAP/Karpenter) + placeholder pods driven by KEDA cron/forecast. Azure Automation adjusts `--min-count`, and `nodepool stop/start` handles dev/test pools.

**(b) Fixed/non-elastic pools (on-prem, bare metal)**
- CAPI (Metal3, OpenShift MachineAutoscaler, or Proxmox/vSphere/KubeVirt providers) with min/max annotations, *or* a power operator over IPMI/Redfish for nodes that keep their identity.
- A forecast/schedule controller sets "awake nodes = forecast + headroom + 1–2 warm standby", and CA or the power operator reacts to pending pods for the remainder.
- Scale-down: cordon → PDB-respecting drain → BMC soft-off after a 30–60 min stabilization window. Never manage the controller's own node, and run the control plane on always-on nodes.

**(c) Hybrid predictive + scheduled + reactive (any environment)**
```
Business metrics (RPS, queue, orders) ─► Prometheus/OTel ─► Forecaster (P90, lead = provision+ready)
Business calendar (campaigns, holidays) ─────────────────────────┘
          ▼
desired_floor = max(schedule, forecast×(1+headroom))          (shadow mode first)
          ▼
Actuator: CapacityBuffer replicas | Karpenter static replicas | node-group min | CAPI | power API
          ▼
Reactive layer: HPA/KEDA on live metrics + CA/Karpenter on pending pods  (covers forecast error)
          ▼
Scale-down governor: stabilization window, step limits, scheduled disruption budgets, PDBs
          ▼
Backtest dashboard: forecast error, pending-pod-seconds, idle node-hours
```

## 9. Pitfalls and Lessons Learned

- **Two writers on one desired-capacity field** (CA + EC2 predictive, CA + VMSS autoscale, or a GKE MIG autoscaler) leads to fights or unsupported states.\[10\]\[22\] Have exactly one actuator per node group and change *floors*, not Desired.\[71\]
- **Placeholder priority below -10** never triggers scale-up. Buffer chunks sized larger than a node never schedule. Pause pods with Karpenter set a hard minimum node count.
- **The /scale gap on CapacityBuffer:** KEDA/HPA can't target it yet, so plan for a patcher or Kedify until #10320 ships.
- **Thrashing:** poorly tuned seasonal models oscillate (the PHPA author's experiment).\[11\] Use hysteresis and asymmetric policies.
- **Scheduler and API saturation:** pre-scaling hundreds of pods at once overwhelmed the scheduler in the CNCF GPU case. Rate-limit.\[12\]
- **Timezones:** Karpenter budget schedules are UTC-only.\[43\] KEDA cron has a `timezone` field.\[72\] Daylight-saving shifts move UTC windows.
- **Dormant projects:** Crane and PHPA haven't released since 2023, and PredictKube depends on a closed SaaS\[73\] whose ongoing availability wasn't verified.\[74\]\[75\]\[76\] Don't put them in a critical path without a fork-and-own plan.
- **Bare metal:** nodes can "wedge" on boot (metalnap added a one-time power-cycle fix).\[63\] BMC credentials are high-value secrets. Silence alerts only for nodes the controller intentionally put to sleep.

## Caveats

- Several 2026 features are alpha, beta or preview (CapacityBuffer in Karpenter and GKE, Karpenter's CAPI provider), and their APIs may change. Verify against the version you run.
- Some figures come from vendor or secondary sources: AWS's 20–40% savings claim, bex.co's CAPI analysis, Medium/oneuptime tutorials, and the GKE active-buffer minimum version (1.35.2-gke.1842000), which was reported only secondhand.\[6\]
- The kube-green v0.7.1 release year (2025) is inferred from its release notes. The current state of the PredictKube scaler in the KEDA 2.21 docs couldn't be checked directly.
- The bare-metal power operators (kube-hardware-autoscaler, metalnap) were found only through their GitHub repos; their adoption and production track record are unknown.

## 資料來源

1. [Prewarm node capacity with Cluster Autoscaler](https://docs.kedify.io/how-to/cluster-autoscaler-capacity-buffers/)
2. [Configuring the cluster autoscaler - OVHcloud Documentation](https://help.ovhcloud.com/csm/en-public-cloud-kubernetes-configure-cluster-autoscaler?id=kb_article_view&sysparm_article=KB0049656)
3. [Cluster Autoscaler Not Scaling Down: Insights & Best Practices](https://www.groundcover.com/learn/cost-optimization/cluster-autoscaler-not-scaling-down)
4. [autoscaler/cluster-autoscaler/FAQ.md at master · kubernetes/autoscaler · GitHub](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
5. [autoscaler/cluster-autoscaler/proposals/buffers.md at master · kubernetes/autoscaler · GitHub](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/proposals/buffers.md)
6. [Instant-On Scaling: Eliminating Node Provisioning Delays in GKE with Capacity Buffers](https://chimbu.medium.com/instant-on-scaling-eliminating-node-provisioning-delays-in-gke-with-capacity-buffers-44ea17bad622)
7. [NodePools](https://karpenter.sh/docs/concepts/nodepools/)
8. [The Azure VM Scale Set (VMSS) autoscaler is not supported for use with AKS cluster node pools - Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/2281577/the-azure-vm-scale-set-vmss-autoscaler-is-not-supp)
9. [About GKE cluster autoscaling | Google Kubernetes Engine (GKE) | Google Cloud Documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
10. [How predictive scaling works - Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-policy-overview.html)
11. [Evaluating Predictive Autoscaling in Kubernetes](https://jamiethompson.me/posts/Evaluating-Predictive-Autoscaling-Kubernetes/)
12. [Scale Before the Spike: Predictive Autoscaling for GPU Workloads on Kubernetes - DEV Community](https://dev.to/ramkumar_nagaraj_38541938/scale-before-the-spike-predictive-autoscaling-for-gpu-workloads-on-kubernetes-5eok)
13. [Scale before the spike: Predictive autoscaling for GPU workloads on Kubernetes](https://www.cncf.io/blog/2026/08/28/scale-before-the-spike-predictive-autoscaling-for-gpu-workloads-on-kubernetes/)
14. [EKS Cluster Autoscaler: 6 Best Practices For Effective Autoscaling - Cast AI](https://cast.ai/blog/eks-cluster-autoscaler-6-best-practices-for-effective-autoscaling/)
15. [Cluster autoscaling in Azure Kubernetes Service (AKS) overview - Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler-overview)
16. [How to Implement Predictive Autoscaling with Kubernetes and ML Models](https://oneuptime.com/blog/post/2026-02-09-predictive-autoscaling-ml-models/view)
17. [Cluster-Autoscaler - EKS Best Practices Guides](https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/)
18. [autoscaler/cluster-autoscaler/cloudprovider/aws/README.md at master · kubernetes/autoscaler · GitHub](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md)
19. [Overprovision Node Capacity For A Cluster](https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning)
20. [Cluster Autoscaler optimization - AWS Prescriptive Guidance](https://docs.aws.amazon.com/es_es/prescriptive-guidance/latest/eks-cost-optimization/5-cluster-autoscaler-optimization.html)
21. [Configure GKE Cluster Autoscaler with Scale-Down Delays to Prevent Flapping](https://oneuptime.com/blog/post/2026-02-17-how-to-configure-gke-cluster-autoscaler-with-scale-down-delays-to-prevent-flapping/view)
22. [Why kOps \`minSize\` and \`maxSize\` Do Not Automatically Scale Nodes](https://oneuptime.com/blog/post/2026-08-01-kops-minsize-maxsize-not-autoscaling/view)
23. [Autoscaling groups of instances | Compute Engine | Google Cloud Documentation](https://docs.cloud.google.com/compute/docs/autoscaler)
24. [Stop and start node pools in Azure Kubernetes Service (AKS) - Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/start-stop-nodepools)
25. [Releases · caas-team/py-kube-downscaler · GitHub](https://github.com/caas-team/py-kube-downscaler/releases)
26. [Announcing kube-green in CNCF landscape](https://kube-green.dev/blog/cncf-landscape/)
27. [kube-green · GitHub](https://github.com/kube-green)
28. [KEDA](https://keda.sh/blog/2023-08-22-keda-cncf-graduation/)
29. [\[keda\] Add KEDA 2.21 by tas50 · Pull Request #11103 · endoflife-date/endoflife.date · GitHub](https://github.com/endoflife-date/endoflife.date/pull/11103)
30. [Scaling Smarter: Instant Nodes, Zero Wait](https://superorbital.io/blog/scaling-smarter-instant-nodes-zero-wait/)
31. [How to Deploy KEDA with Cron Trigger with Flux CD](https://oneuptime.com/blog/post/2026-03-13-deploy-keda-cron-trigger-flux-cd/view)
32. [cron-scaler scales higher than expected · Issue #5820 · kedacore/keda · GitHub](https://github.com/kedacore/keda/issues/5820)
33. [Scale to zero with cron trigger · kedacore/keda · Discussion #1759 · GitHub](https://github.com/kedacore/keda/discussions/1759)
34. [CapacityBuffers](https://karpenter.sh/docs/concepts/capacitybuffers/)
35. [New GKE active buffer minimizes scale-out latency](https://cloud.google.com/blog/products/containers-kubernetes/new-gke-active-buffer-minimizes-scale-out-latency)
36. [Release cluster-autoscaler-1.35.0 · kubernetes/autoscaler · GitHub](https://github.com/kubernetes/autoscaler/releases/tag/cluster-autoscaler-1.35.0)
37. [Scaling GKE Capacity Buffers](https://docs.kedify.io/how-to/gke-capacity-buffers/)
38. [Give CapacityBuffers the /scale subresource by Denton-L · Pull Request #10320 · kubernetes/autoscaler · GitHub](https://github.com/kubernetes/autoscaler/pull/10320)
39. [karpenter/designs/static-capacity.md at main · kubernetes-sigs/karpenter · GitHub](https://github.com/kubernetes-sigs/karpenter/blob/main/designs/static-capacity.md)
40. [EKS Auto Mode의 정적 용량 노드 풀 - Amazon EKS](https://docs.aws.amazon.com/ko_kr/eks/latest/userguide/auto-static-capacity.html)
41. [Automatically scale StaticCapacity replicas when future ODCRs/Capacity Blocks become active · Issue #9001 · aws/karpenter-provider-aws · GitHub](https://github.com/aws/karpenter-provider-aws/issues/9001)
42. [Karpenter Disruption and Drift: How to Consolidate Nodes Safely](https://cast.ai/blog/karpenter-disruption-drift/)
43. [Karpenter: an introduction to the Disruption Budgets - RTFM](https://rtfm.co.ua/en/karpenter-an-introduction-to-the-disruption-budgets/)
44. [Support AWS Warm Pools for karpenter · Issue #4354 · aws/karpenter-provider-aws · GitHub](https://github.com/aws/karpenter-provider-aws/issues/4354)
45. [ADVPERF02-BP03 Consider using low latency scaling tools like Karpenter to improve startup and scaling time - Video Streaming Advertising Lens](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf02-bp03.html)
46. [Amazon EKS Managed Node Groups Now Support EC2 Auto Scaling Warm Pools](https://builder.aws.com/content/3CFwqjLgJxY6VVjZctgXgGbqatp/amazon-eks-managed-node-groups-now-support-ec2-auto-scaling-warm-pools)
47. [Amazon EKS managed node groups now support EC2 Auto Scaling warm pools](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-eks-managed-node-groups-ec2-warm-pools)
48. [node auto provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning?authuser=3)
49. [Scaling based on predictions](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling?authuser=1)
50. [Autoscaling Guidance - Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/best-practices/auto-scaling)
51. [Scaling solution for workloads and compute resources in ACK clusters - Container Service for Kubernetes - Alibaba Cloud Documentation Center](https://www.alibabacloud.com/help/en/ack/ack-managed-and-ack-dedicated/user-guide/auto-scaling-overview/)
52. [Predict & Scale Pods Beyond Standard HPA with AHPA - Container Service for Kubernetes - Alibaba Cloud](https://www.alibabacloud.com/help/en/ack/ack-managed-and-ack-dedicated/user-guide/ahpa-overview-1/)
53. [Perform intelligent scalability predictions and resource prefetching to prevent service scaling delays - Container Service for Kubernetes - Alibaba Cloud Documentation Center](https://www.alibabacloud.com/help/en/ack/ack-managed-and-ack-dedicated/user-guide/deploy-ahpa)
54. [\[2604.19705\] Predictive Autoscaling for Node.js on Kubernetes: Lower Latency, Right-Sized Capacity](https://arxiv.org/abs/2604.19705)
55. [AAPA: An Archetype-Aware Predictive Autoscaler with Uncertainty Quantification for Serverless Workloads on Kubernetes](https://arxiv.org/html/2507.05653v2)
56. [Autoscaling - The Cluster API Book - Kubernetes](https://release-1-3.cluster-api.sigs.k8s.io/tasks/automated-machine-management/autoscaling)
57. [Karpenter's Alpha Cluster API Provider vs. Cluster Autoscaler: What Actually Autoscales an Owned-Hardware Kubernetes Fleet in 2026](https://bex.co/blog/2026/07/09/karpenter-capi-cluster-autoscaler-bare-metal)
58. [How to Scale Cluster Node Pools with Cluster API and Flux](https://oneuptime.com/blog/post/2026-03-13-scale-cluster-node-pools-with-cluster-api-and-flux/view)
59. [Scale a node pool in Syself Autopilot](https://syself.com/docs/hetzner/apalla/servers-and-nodes/pools/scale-a-pool)
60. [A guide to the OpenShift cluster autoscaler with Mapi baremetal](https://www.redhat.com/en/blog/a-guide-to-the-openshift-cluster-autoscaler-with-mapi-baremetal)
61. [GitHub - safewords/kube-hardware-autoscaler: Kubernetes operator that powers bare-metal nodes on and off based on demand: IPMI, Redfish, PiKVM, NanoKVM, JetKVM and Wake-on-LAN, with fallback and safety checks. · GitHub](https://github.com/safewords/kube-hardware-autoscaler)
62. [GitHub - mgd43b/metalnap: Suspend idle bare-metal Kubernetes nodes to save power, without killing running work. Drains gracefully, wakes on demand, powers over IPMI. · GitHub](https://github.com/mgd43b/metalnap)
63. [fix: power-cycle wedged nodes once, and mute only what metalnap put down by mgd43b · Pull Request #15 · mgd43b/metalnap · GitHub](https://github.com/mgd43b/metalnap/pull/15)
64. [Autoscaling bare metal clusters · Issue #1060 · kubernetes/autoscaler · GitHub](https://github.com/kubernetes/autoscaler/issues/1060)
65. [BMC Communication: IPMI vs Redfish Guide](https://www.thnkbig.com/blog/bmc-communication-ipmi-redfish/)
66. [IPMI Guide - KubeVirtBMC Documentation](https://docs.kubevirtbmc.io/ipmi-guide/)
67. [Configuring the cluster autoscaler - Support Guides - OVH](https://support.us.ovhcloud.com/hc/en-us/articles/1500009132502-Configuring-the-cluster-autoscaler)
68. [Karpenter Best Practices for Cost, Reliability, and Safe Scaling](https://cast.ai/blog/karpenter-best-practices/)
69. [How to Set Up AKS Cluster Autoscaler with Custom Scale-Down Delay](https://oneuptime.com/blog/post/2026-02-16-how-to-set-up-aks-cluster-autoscaler-with-custom-scale-down-delay-and-utilization-thresholds/view)
70. [Scale Kubernetes deployments to zero using KEDA - Mijndert Stuij](https://mijndertstuij.nl/posts/scale-to-zero-keda-cron-scaler/)
71. [VMSS Predictive Autoscale and AKS](https://learn.microsoft.com/en-us/answers/questions/1659645/vmss-predictive-autoscale-and-aks)
72. [KEDA CRON Scaling - KodeKloud](https://notes.kodekloud.com/docs/Kubernetes-Autoscaling/Kubernetes-Event-Driven-Autoscaling-KEDA/KEDA-CRON-Scaling/page)
73. [Predictkube](https://keda.sh/docs/2.19/scalers/predictkube/)
74. [Predictkube](https://keda.sh/docs/2.14/scalers/predictkube/)
75. [predictive-horizontal-pod-autoscaler command - github.com/jthomperoo/predictive-horizontal-pod-autoscaler - Go Packages](https://pkg.go.dev/github.com/jthomperoo/predictive-horizontal-pod-autoscaler)
76. [Releases · gocrane/crane](https://github.com/gocrane/crane/releases)