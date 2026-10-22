# Tablet-Style Payment & SaaS Devices: A Hardware PM's Landscape, Use-Case and Regional Market Report (October 2026)

Android smart terminals have won the platform war in tablet-style POS. Counterpoint Research's Global POS Device Tracker & Forecast (Aug 13, 2026) found that "around 48% of all POS terminals shipped in 2025 were Android-based" and projects about 70% by 2032. A small group of Chinese OEMs builds most of these devices: PAX, Sunmi, Centerm, Newland, Landi and Castles, with iMin, Urovo and Telpo behind them. The brands merchants see (Square, Toast, Clover, stera, Mercado Pago, PagBank and others) mostly decide how the device is sold: bundled, subsidized, financed or rented. Where you compete depends on region. North America is a SaaS-bundled, Toast/Square/Clover market; Japan runs on acquirer-rented Android terminals plus iPad registers; Korea runs on Windows POS plus VAN card readers and is starting to move; Southeast Asia is QR-first, with few dedicated terminals; Brazil is the world's densest subsidized smart-POS market.

## TL;DR
- **The market is flat in volume but the platform is shifting.** Global POS shipments "remained largely flat, growing just 1% YoY in 2025," held back by memory-chip prices, tariffs and inflation (Counterpoint Research Director Mohit Agrawal, Aug 2026). Android took about 48% of those shipments. PAX now earns over 70% of its revenue from Android (FY2025). Sunmi, which China Insights Consultancy (cited in its prospectus) ranks as the largest Android "business IoT" vendor with over 10% share by 2024 revenue, listed in Hong Kong in April 2026 (06810.HK, HK$24.86 per share). Rising memory prices are the main near-term pressure on bill-of-materials cost and average selling price.
- **Where the money is: North America (high ASP, SaaS-bundled) and Brazil (huge installed base, subsidized).** Toast runs about 180,000 locations (Q2 2026). Square Register sells for $899. Clover Station Duo 2 lists at about $1,895 at resellers. Brazil has over 35M POS terminals (2024), but Pix took 34% of in-store payment value in 2025 (Worldpay Global Payments Report, Mar 2026). Japan (stera ~330k units at end-2023, target 1M by 2030) and Korea (3.21M merchants; Toss Place passed 100k merchants in Feb 2025) are replacement and upgrade markets. In Southeast Asia, QR acceptance points outnumber terminals by an order of magnitude (Indonesia: 42M QRIS merchants vs 2.42M EDC units in 2025).
- **What to build:** a modular Android 13/14+ platform on Qualcomm QCM-class or MediaTek silicon, with PCI PTS 7.x, EMVCo contactless kernel C-8 and MPoC-ready software. Offer three form factors: a 6–6.5" rugged handheld, a 7–8" customer-facing tablet, and a 14–15.6" dual-screen countertop with an 80mm printer. Make remote fleet management the product, and design for GMS-EDLA/locked-down Android variants and memory-cost volatility.

## Key Findings

**1. Platform consolidation.** Counterpoint (Aug 13, 2026) reports 1% growth in global POS shipments in 2025 and about 48% Android share. It forecasts a 4% CAGR for all POS through 2032 against 6% for Android, with Android reaching about 70% of shipments by 2032. Proprietary OSes such as Verifone VOS2/Engage and Ingenico Telium/TETRA "continue to lose relevance." Counterpoint expects SoftPOS to "absorb demand at the low end" but not to displace attended and unattended terminals.\[1\] Berg Insight's earlier estimate was that about 40% of POS terminals sold in 2023 ran Android, with Sunmi, Tianyu (Centerm), PAX, Verifone, Castles, Ingenico, Landi and Newland as the leading Android vendors.\[2\]

**2. Chinese OEM concentration.**
- PAX FY2025:
  - Revenue was HK$5,872.5M (−2.9%) and net profit HK$756.2M (+4.9%).\[3\]
  - Android products were over 70% of revenue, and PAX sold over 4M Android SmartPOS units in 2025.\[4\]\[5\]
  - It has shipped 117M+ terminals overall and 23M+ Android SmartPOS units cumulatively.\[5\]
  - MAXSTORE, its remote-management and app platform, connected over 16M terminals at end-2025; the corporate site now says 18M+.\[4\]\[5\]
- Sunmi:
  - Revenue was RMB 3.071bn, 3.456bn and 3.812bn for 2023–2025, with 74.9% from outside China in 2025.\[6\]\[7\]
  - Its prospectus reported about 4.9 million monthly active devices as of Dec 31, 2024 (up from 3.2M at end-2022); IPO-launch coverage (uSmart, Apr 2026) cites about 6 million.
  - Its largest Brazilian customer, now in an arbitration dispute with Sunmi, was 22.0% of 2024 revenue.\[8\]
- Brand concentration therefore sits on top of real manufacturing concentration. Most Western "first-party" devices are ODM-built or built on these platforms; the Japanese stera terminals, by contrast, are co-developed with Panasonic Connect.\[9\]\[10\]

**3. Memory costs are the 2026 hardware story.** PAX's FY2025 presentation flags a "significant rise in memory chip prices since Q4 2025" and says it will "adjust pricing as needed."\[11\] Counterpoint says Android SmartPOS, with its higher RAM/flash, is the most exposed category, and expects price adjustments and longer lead times for high-memory configurations.\[1\] That works directly against the spec race to 6–8GB RAM (Sunmi T3 Pro Max: 6GB/128GB; Square Register 2nd gen: 8GB/128GB).\[12\]\[13\]

**4. The device is sold through the business model.** Square Register costs $899 or $44/month over 24 months.\[13\] Clover devices are often "placed" for $99 by ISOs tied to processing.\[14\] Mercado Pago in Mexico lists the Point Smart 2 at MXN 4,499 but sells it for MXN 549, and refunds the device cost once the merchant processes MXN 30,000.\[15\]\[16\]\[17\] In Brazil, an analyst estimate puts PagBank's roughly R$1.8bn annual depreciation largely on its POS fleet.\[18\] Hardware is a customer-acquisition cost, and the PM's job is to minimize total cost of ownership per active merchant, not to maximize margin per unit.

**5. Regional penetration diverges sharply** (detail below).
- Japan:
  - The old cashless metric reached 42.8% in 2024; under METI's revised measure the ratio was 58.0% in 2025 (¥162.7tn).\[19\]\[20\]
  - Targets are 65% by 2030 and 80% long-term.\[20\]
- Korea: card acceptance is near-universal across about 3.21M merchants, and the FSC caps preferential MDRs at 0.4–1.45% (Aug 2025).\[21\]\[22\]
- Indonesia: QRIS reached 42M merchants at end-2025 against 2.42M EDC machines.\[23\]\[24\]
- Brazil: in-store card payments are 73.6% contactless (ABECS 2025), and Pix took 34% of in-store value in 2025 (Worldpay Global Payments Report, published Mar 31, 2026; 32% in 2024).

## Landscape and Taxonomy of Device Archetypes

| Archetype | Typical display | Payments | Typical buyer | Examples |
|---|---|---|---|---|
| A. Countertop all-in-one, dual screen | 14–15.6" merchant + 8–15.6" customer | Integrated EMV/NFC/MSR or via a customer-facing payment tablet | SMB merchant via platform/ISO; chains via ISV | Clover Station Duo 2, Square Register, Sunmi T3 Pro/Max, Toast Flex 3 + Guest Display, iMin Swan/Falcon, PAX Elys station |
| B. Customer-facing payment tablet (7–8") | 7–8" | PCI PTS PIN-on-glass/keypad, EMV/NFC/MSR | ISV/acquirer | PAX A3700, Clover Mini, stera terminal standard (7" + 4") |
| C. Kiosk / KDS / signage | 15.6–32" | Embedded unattended payment module (e.g., PAX IM30) or none | Franchisor/enterprise | Toast Kiosk, Toast Flex for Kitchen (22"), Sunmi K2, Square Kiosk |
| D. Commercial/rugged tablet for LOB SaaS | 8–11" | Usually none; paired reader or Tap to Pay | Enterprise IT | Samsung Galaxy Tab Active, Zebra ET-series (specs not verified in this research) |
| E. Consumer tablet + enclosure | 8.3–13" iPad/Galaxy Tab | Bluetooth reader, Tap to Pay on iPhone/Android | Micro/SMB | iPad + Square Stand ($149), Airレジ/Smaregi on iPad in Japan |
| F. Handheld smart POS (secondary category) | 5.5–6.5" | Integrated, often with printer | Acquirer/platform | Toast Go 3, Square Handheld, Clover Flex 4, PAX A920Pro, Mercado Pago Point Smart 2, stera terminal mobile |

## Manufacturer and Platform Profiles with Model Tables

### Primary category: tablet/countertop devices (≥7")

| Maker / model | Status | Display(s) | SoC / RAM / storage | OS / management | Payments & certs | Connectivity / I/O | Price (date) |
|---|---|---|---|---|---|---|---|
| **Sunmi T3 Pro Max** (P0125xxxx) | Shipping (first listed Dec 2023) | 15.6" FHD 1920×1080, 400 nits, rotating; optional 15.6" FHD or 10.1" HD (1280×800) customer display | Qualcomm "Kryo-670" octa-core up to 2.7GHz, 6nm (exact QCM part number not verified); 6GB/128GB; microSD to 2TB | SUNMI OS based on Android 13; GMS-EDLA variants | NFC built into screen; SoftPOS app support; no PCI PTS PIN entry on the AIO itself (not verified) | Wi-Fi 6 (802.11ax), BT 5.2, gigabit LAN, 4–6 USB, RJ11/RJ12 cash drawer; built-in 80mm printer 250mm/s with auto-cutter; 8MP camera; 3.3kg | US street $1,282–$1,802; UK £1,559.99; EU €1,634 (2025–26 retailers)\[12\]\[25\]\[26\]\[27\]\[28\]\[29\] |
| **Sunmi T3 / T3 Pro** | Shipping | 15.6" FHD | T3: Qualcomm QCM4325, 4GB/64GB; T3 Pro: 6GB/128GB | Android-based SUNMI OS, GMS-EDLA | NFC (GMS variant) | Optional 80mm printer (T3 80mm variant) | Not verified\[30\] |
| **Clover Station Duo 2** (Fiserv) | Shipping (launched June 2023; replaced Duo 1)\[31\] | 14.0" IPS FHD merchant + 8.0" IPS HD customer\[32\] | Qualcomm Snapdragon 660 (4×1.8 + 4×2.2GHz); 2GB/16GB\[32\] | Clover-hardened AOSP Android 10 (Duo 1: 8.1); Clover App Market\[31\]\[32\] | EMV, NFC, MSR (500k inserts/swipes); PCI PTS 6.x; Apple/Google/Samsung Pay\[31\]\[33\] | Ethernet, Wi-Fi, 4G/LTE (NA/EU); 4 USB, 2 RJ12 cash drawer; dual 5MP cameras with Zebra scanning software; 80mm (3⅛") thermal printer\[32\]\[34\] | Reseller list $1,895, sale $1,295; "placement" $99 with processing contract (2026)\[14\]\[35\] |
| **Square Register (2nd gen)** (Block) | Shipping | Dual screens (sizes not captured) | Up to 2.7GHz, 8GB RAM, 128GB flash (SoC not disclosed)\[13\] | Square proprietary Android-based OS (not verified) | Tap/dip/swipe on customer display\[13\] | Upgraded Wi-Fi chip/antenna; IP54\[13\] | US $899 or $44/mo × 24; kits $1,189–$1,799; AU A$1,099\[13\]\[36\]\[37\] |
| **PAX A3700 (Elys Tablet)** | Shipping | 7" IPS 1280×800 | Octa-core 1.8GHz (benchmarks show MediaTek MT6762, i.e., Helio P22-class); 2GB / 16 or 64GB; microSD to 256GB | Android 11; PAXSTORE/MAXSTORE | EMV/NFC/MSR, PIN; PCI PTS 6.x SRED | Dual-band Wi-Fi, BT 5.0, optional 4G, USB-C, pogo dock to Elys L1400 workstation (USB-A, RS232, cash drawer, printer, LAN); 5MP camera; 3720mAh; 787g | ~US$505 (reseller, 2026)\[38\]\[39\]\[40\]\[41\]\[42\]\[43\] |
| **stera terminal standard** (SMBC; Panasonic Connect) | Shipping since July 2020 | Staff 7.0" 1280×720 + customer 4.0" 800×480 | Not disclosed | Android; "stera market" app store | Credit, e-money (FeliCa), QR — 30+ payment brands | Built-in printer; serial link to POS; 956g | Acquirer-bundled (stera pack); MDR from 1.98% (V/MC small-business plan)\[44\]\[45\]\[46\]\[47\] |
| **Toast Flex 3 + Guest Display**; **Toast Flex for Kitchen (22")** | Shipping | Flex 3 terminal (size not captured); guest display; 22" KDS | Not disclosed | Toast Android (locked) | Integrated via guest display/Toast Tap | — | Flex third-party estimate $799–$999 (not official)\[48\] |

### Secondary category: handheld smart POS

| Maker / model | Launch | Display | Key specs | Price |
|---|---|---|---|---|
| **Toast Go 3** | US July 31, 2025; global Apr 28, 2026\[49\]\[50\] | 6.52" HD TFT, 550 nits\[51\] | IP65, 5ft/1.5m drop, 24+ h battery (4.5 h charge), 426g, 189×90×35mm, 5MP front/8MP rear, Wi-Fi 6 2×2 MIMO, optional 4G, swipe/dip/tap, PIN-on-glass, PCI PTS, E2EE; 16% lighter than Go 2\[51\]\[52\]\[53\] | Not published (Go 2 third-party estimate $409–$609)\[48\] |
| **Square Handheld** | May 13, 2025\[54\] | 6.2" Gorilla Glass\[55\] | 11 oz/315g, 15.7mm, IP54, 16MP camera barcode scanning, tap/chip\[55\]\[56\]\[57\] | US $399 ($37/mo × 12); AU A$349; EU from €199 + VAT\[13\]\[37\]\[57\] |
| **Clover Flex 4** | Shipping | 5.99" (Flex 3 per reseller)\[33\] | Built-in printer and camera scanner\[33\] | Bundled/placed |
| **PAX A920Pro** | Refreshed 2025 | — | PCI PTS POI v7.0, EMVCo Contactless Kernel C-8 (PAX FY2025)\[4\] | Not verified |
| **PAX A950, A6630, A77** | 2025 launches | — | New Android models named in FY2025 results; specs not verified\[58\] | — |
| **stera terminal mobile / unit** | 2024 | 5.5" 1440×720 | Mobile: 300g, ~17mm; Unit: 370g, POS/kiosk-embedded | Acquirer-bundled\[9\]\[44\]\[46\] |
| **Mercado Pago Point Smart 2** (Mexico) | Shipping | "Largest touch screen" in MP line | Integrated printer, free data connection | MXN 549 (list MXN 4,499; Oct 2026); Amazon MX MXN 399\[16\]\[17\]\[59\] |

**Specs not verified in this research:** Verifone (Carbon, M440/T650), Ingenico Axium DX8000/EX8000, iMin, Castles Saturn/S1F2, Newland, Elo, Zebra, Samsung Tab Active, Shopify POS Terminal, Stripe S700, Smaregi/Airレジ hardware. Treat any values cited for these from memory as unconfirmed.

## Device Images

Only image URLs actually retrieved during research are embedded. For other devices, the official product page that shows the device is named.

![Square Register (2nd gen) with phone tap — Square official](https://images.ctfassets.net/2d5q1td6cyxq/4RVkJmjVdBA8p9cthDU0Bc/dafc275105042df4ca6626caf5758620/Register_X2c_Phone_Tap__-_USEN.png?w=1200&h=630&fit=thumb&fm=jpg&q=90)
*Square Register (2nd gen). Source: squareup.com hardware page.*

![Toast hardware share image — Toast official (may be a generic brand image, not specifically Toast Go 3)](https://d2w1ef2ao9g8r9.cloudfront.net/images/otl.jpg)
*Toast Go 3 product page share image (pos.toasttab.com/hardware/toast-go). Flag: this may be a generic image.*

![Counterpoint: Global POS shipments by OS, 2025 vs 2032F](https://static.counterpointresearch.com/statics/images/admin/4f20dd50-9714-11f1-8f75-ed34835d6f34.jpg)
*Counterpoint Global POS Device Tracker chart (Aug 2026).*

Official product pages with images (image file URLs not captured):
- Clover Station Duo 2: docs.clover.com device specs.
- PAX A3700: buy.posportal.com.
- Sunmi T3 Pro Max: sunmi.cz and ics.gr.
- stera terminal series: smbc-card.com/kamei/stera/terminal.
- Mercado Pago Point Smart 2: mercadopago.com.mx/herramientas-para-vender/lectores-point/point-smart.
- Square Handheld: squareup.com press page.

## Use-Case Analysis (Hardware PM Lens)

| Scenario | Hardware requirements | Archetype chosen | Buyer | Business-model effect |
|---|---|---|---|---|
| **Full-service restaurants** | Rugged handhelds (IP65, 5ft drop, 24h battery, LTE for patios),\[52\] 14–15.6" host stations, 22" KDS, guest display | F + A + C | Merchant via vertical SaaS (Toast), franchisor | SaaS lock-in: Toast hardware runs only Toast.\[48\] The handheld is the upsell engine (Go 3 + ToastIQ prompts).\[60\] |
| **QSR / fast casual** | Self-order kiosks, KDS, drive-through handhelds, countertop with 80mm printer | C + A + F | Franchisor/enterprise IT | Enterprise wins (Applebee's, TGI Fridays UK) pull standardized fleets. Remote management and uptime SLAs matter more than unit price.\[61\]\[62\] |
| **Cafés / micro F&B** | 8–15.6" AIO or iPad + reader; small footprint | A, E, F | Owner | Square/Clover financing ($37–$44/mo) and $99 placements; in Korea, Toss Front/Terminal with kiosk mode.\[63\] |
| **Retail (general/specialty)** | Dual screen for item review, camera/scanner, cash drawer, scale port; handheld for line-busting and inventory | A + F | Merchant/ISV | Square Register Retail Kit $1,799;\[36\] handheld doubles as inventory scanner (16MP camera).\[56\] |
| **Grocery/convenience** | Windows/Linux lanes, integrated scanners/scales, PIN pads; Android for assisted/self-checkout | Legacy + B | Chain IT | Slowest to move to Android; payment tablets (B) attach to existing lanes. |
| **Hospitality/hotels/venues** | Check-in kiosks, F&B handhelds, stadium high-throughput tap | C + F | Enterprise/franchisor | BWH Hotels endorsed Toast for thousands of properties (Q2 2026); PAX cites sports venues for A920Pro/A35/A800.\[62\]\[64\] |
| **Services (salons, gyms, home services)** | Handheld or phone (Tap to Pay), appointment SaaS | F, E, SoftPOS | Owner | SoftPOS cannibalizes dedicated hardware most here. Toss Place: beauty is 19% of its merchants.\[65\] |
| **Healthcare check-in / co-pay** | 7–10" customer-facing tablet, privacy, PCI PTS | B, D | Practice/ISV | Semi-integrated payments keep card data out of PM/EHR software scope. |
| **Unattended (EV charging, vending, transit)** | Embedded modules, outdoor ratings, open-loop EMV | Unattended (PAX IM30), stera terminal unit | Operator | PAX: EV-charging partnerships drove IM30 growth (H1 2025).\[66\] Seoul installed 440 card-accepting subway kiosks at 273 stations.\[46\]\[67\] |
| **Micro-merchants/street vendors** | Low cost, printer, cellular SIM, long battery, QR display | F (Point Smart 2, Ton, Moderninha) or QR sticker | Acquirer/platform | Device sold below cost or refunded against volume (Mercado Pago MXN 30,000 threshold).\[15\] |
| **Non-payment SaaS (queue, table mgmt, time clock, signage)** | Cheap Android/iPad, kiosk mode, MDM | D, E, C | Ops/IT | Android POS app stores (MAXSTORE, Clover App Market, stera market) monetize installed bases. |

**Strategic shapers:**
1. **Integrated vs. semi-integrated payments.** Fully integrated platforms (Toast, Square, Clover) subsidize hardware and capture payments revenue. Semi-integrated ISVs buy PAX/Verifone/Ingenico payment tablets (archetype B) to stay out of PCI scope.
2. **SoftPOS/MPoC** (stera tap, Japan's first MPoC-certified solution, at 2.7% MDR) erodes the sub-$100 reader and micro-merchant handheld tier.\[9\]\[68\] It does not erode the countertop/kiosk tier.\[1\]
3. **Remote fleet management** (MAXSTORE 16M+, Sunmi ~4.9M monthly active devices at end-2024 per its prospectus, ~6M per IPO coverage) is the actual moat, and the base for SaaS revenue.

## Region-by-Region Market Analysis

### North America (US, Canada)
- **Penetration and structure:** card acceptance is universal. The battle is software-led replacement of legacy ECR/Windows POS and plain terminals by SaaS-bundled Android devices and iPads.
- **Toast:**
  - About 180,000 locations at Q2 2026 (+22% YoY), with a record ~9,500 net adds in the quarter.\[62\]
  - Record 30,000 net adds in 2025.\[69\]
  - GPV $60.7bn in Q2 2026; ARR $2.4bn.\[62\]
- **Clover:** Fiserv cut its 2025 Clover revenue guidance from $3.5bn to $3.3bn in Q3 2025, and Clover finished 2025 at $3.3bn (+23%).
- **Square:** restaurants and retailers drove 50% of Square GPV in 2024.\[55\]
- **Prices:** Square Register $899; Square Handheld $399; Square Stand $149 (the iPad route);\[13\] Clover Station Duo 2 $1,295–$1,895 (reseller);\[35\] Sunmi T3 Pro Max $1,282–$1,802; PAX A3700 ~$505.\[28\]\[29\]\[43\] Industry smart-POS price band: US$249–$599 for Android handheld/tablet smart terminals (Coherent Market Insights pricing analysis).\[70\]
- **Commercial models:** purchase, 12–24-month 0% financing, ISO placement ($99), and bundles tied to SaaS plans (Clover software plans $0–$84.95/month at resellers).\[14\]\[71\]\[72\]
- **Installed-base estimate (derived, low–medium confidence):**
  - Toast: 180k locations × an assumed 4–6 Toast devices per location gives ~0.7–1.1M Toast devices.
  - Square, Clover, Lightspeed/Shopify iPad estates, and ISV-deployed PAX/Ingenico/Verifone smart terminals likely add a combined base of several million.
  - Total North American smart/tablet POS (including iPads used as POS): roughly 8–14M devices. Method: platform location counts × devices per site, plus an iPad-POS allowance. Confidence: low, because Square and Clover do not disclose device counts.

### Japan
- **Penetration:**
  - METI's cashless ratio was 42.8% in 2024 (¥141.0tn) on the legacy metric.\[19\]
  - For 2025, METI changed the denominator and reported 58.0% (¥162.7tn).\[20\]\[73\] The two numbers are not a like-for-like jump.\[74\]
  - Targets: 65% by 2030, 80% long-term.\[20\]
  - Tokyo was already at 60.7% by value (FY2024, Tokyo Metropolitan Government).\[73\]
- **Ecosystem:**
  - SMBC's stera terminal (Android, built by Panasonic Connect, which says it holds about 70% of Japan's payment-terminal market per JEITA statistics and has shipped 3M+ terminals cumulatively) reached about 330,000 units by end-2023. SMBC targets 1M stera units by 2030; its site cites 550,000 cumulative "stera adoptions" (likely contracts, not devices).\[44\]\[68\]\[75\]
  - iPad POS dominates SMB software: Airレジ (Recruit) had 904,000 registered accounts (Sept 2024); Smaregi had 56,719 active stores (Apr 2026); Ubiregi claims 40,000+ stores. An iPad costs ¥58,800+.\[76\]\[77\]\[78\]\[79\]
  - PAX names Japan as its "primary revenue contributor" in APAC (FY2025 APAC revenue HK$1,112.5M, +4.5%).\[3\]\[80\]
- **Usage:** multi-brand acceptance (credit, FeliCa e-money, QR such as PayPay) on one Android terminal is the key requirement; it is why one Android device beats separate readers.\[45\]\[47\]
- **Installed-base estimate (derived, medium-low confidence):** Android smart payment terminals of ~0.8–1.2M in 2026, i.e., stera at ~0.45–0.6M (extrapolating 330k in 2023 toward the 1M target) plus PAX, Square and other acquirer fleets. Separately, ~0.6–1.0M iPads in POS use (Airレジ accounts overstate active devices).

### South Korea
- **Penetration:**
  - Card acceptance is effectively universal; about 3.21M card merchants, 95.7% of which qualify for FSC-capped preferential MDRs of 0.4–1.45% (effective Aug 14, 2025).\[21\]
  - Mobile payments are 54.3% of card spend (Bank of Korea, 2025).\[21\]
  - The legacy stack is Windows POS (POSReady/Win10 IoT on Intel Atom, e.g., OKPOS/POSBANK units certified via VAN operators such as KOVAN) plus separately certified card readers routed through VANs. Domestic acquiring requires a licensed Korean PG/VAN.\[21\]\[81\]
- **Disruptor:** Toss Place, which sells the Android-based Toss Front (customer) and Toss Terminal with Toss POS software, passed 100,000 merchants in Feb 2025, two years after its March 2023 launch.\[63\]\[65\]
  - It was adding 8,000+ merchants a month, which it says is over 25% of roughly 30,000 new merchant openings per month.\[82\]
  - Its merchants are restaurants (48%), cafés (20%) and beauty (19%).\[83\]
  - Cumulative volume: 260M transactions, KRW 7.7tn.\[84\]
  - A kiosk mode on the same hardware displaces separate kiosks.\[63\]
- **Installed base:** Ken Research estimates 5.25M active POS units (2025; third-party, low confidence).\[85\]
- **Derived estimate:** Android smart POS at ~0.3–0.6M units (Toss Place extrapolated at its early-2025 pace to ~0.2–0.3M merchants by late 2026, plus Android kiosks and table-order devices). Confidence: low.
- **Implication:** Korea is a replacement market where certification (Korean card terminal security certification), VAN integration and kiosk/table-order bundles matter more than EMV/PCI branding.

### Southeast Asia
- **Penetration (central-bank data):**

| Country | Dedicated terminals | QR acceptance | Date / source |
|---|---|---|---|
| Indonesia | 2,422,351 EDC (2025); 2,360,702 (Sep 2026)\[23\] | 42M QRIS merchants (end-2025), ~90% MSMEs; 2026 target 45M\[24\] | Bank Indonesia SPIP; BI |
| Thailand | 900,000+ EDC (37% in Bangkok)\[86\] | 1M+ QR acceptance points\[87\] | Bank of Thailand × Visa whitepaper (c. 2025) |
| Malaysia | ~0.98M POS terminals (Jul 2024)\[88\] | DuitNow QR ~3M locations (2025)\[89\] | BNM presentation; BNM Annual Report 2025 |
| Philippines | 316,795 terminals (2025, +12.9%): 168,565 mPOS (+20.5%), 148,230 traditional\[90\] | QR Ph (not captured) | BSP E-Payments Measurement Report 2025 |
| Vietnam | POS +19.9% in 2025 (secondary aggregator); last SBV count found 277,754 (Dec 2019)\[91\]\[92\] | VNPAY/VietQR dominant | SBV via secondary source, low confidence |
| Singapore | Not found | NETS/SGQR | No data captured |

- **Indonesia bank fleets:** BCA had 656k+ EDCs (Dec 2023); Mandiri ~256k and BNI ~260k (early 2025).\[93\]\[94\] BCA is deploying Android POS ("APOS") with contactless.\[93\]
- **Vendors:**
  - PAX cites "softer demand in parts of Southeast Asia due to macroeconomic headwinds and extended sales cycles" (FY2025).\[80\]
  - Sunmi's rest-of-APAC (ex-China) revenue was RMB 313M, or 17.7% of H1 2026 revenue (secondary report of its interim results).\[95\] Southeast Asia is not broken out.
  - iMin (Singapore) opened its first Malaysian factory in Johor (Aug 2024, MIDA) and supplies Swan 2/Swift 2 to LINE MAN Wongnai in Thailand.\[96\]\[97\] It discloses no unit numbers.
- **Price/commercial model:** bank-rented EDCs (free with merchant account) and acquirer- or super-app-subsidized Android devices for F&B chains. For micro-merchants the QR sticker costs effectively zero, which caps dedicated-hardware demand. Smart POS price band US$249–$599 (global pricing analysis).\[70\]
- **Installed-base estimate (derived, low–medium confidence):**
  - Dedicated terminals across the six markets: ~5.0–5.5M (ID 2.4M + TH 0.9M + MY ~1.0M + PH 0.32M + VN ~0.4–0.6M (est.) + SG ~0.1–0.2M (est.)).
  - Android smart share: ~25–40% (BCA APOS migration, Philippine mPOS growth), i.e., ~1.3–2.2M smart/Android payment terminals.
  - Non-payment Android POS/ordering tablets (Sunmi/iMin in F&B) are not counted above and could add a similar magnitude.

### South America (with Mexico labeled as LatAm context)
- **Brazil:**
  - Installed base: over 35M POS terminals in 2024 (Statista).\[98\]
  - Card volume: R$4.5tn in 2025 (ABECS).\[99\] Contactless was 73.6% of in-person card purchases in 2025, with 42.6% of credit purchases in installments (ABECS).\[100\]
  - Pix: 34% of point-of-sale value in 2025, mostly QR (Worldpay 11th Global Payments Report, published Mar 31, 2026; up from 32% in 2024). Contactless Pix was only 1.06M transactions in Jan 2026 versus 6bn+ Pix transactions overall.
  - Terminal market value: IHL sizes it at US$821M (2025) → ~US$1.0bn (2030), with 68% contactless terminal penetration.\[101\]
  - Acquirer shares (2025): Stone 10.3% of ABECS volume (13.8% excluding e-commerce; 20-F). Cielo (~25–30%) and Rede (~26%) per lower-quality secondary sources. PagBank has a mid-teens share of active merchants (analyst estimate). InfinitePay (CloudWalk) has ~6M merchants (Sacra).\[18\]\[99\]\[102\]\[103\]
  - Commercial model: acquirer-subsidized "maquininhas," sold outright cheaply or rented; Cielo/Rede have phased out rental fees. Cielo launched Brazil's first smart POS, Cielo LIO, in 2016.\[102\]\[104\]
  - Smart-terminal supply signal: Sunmi's largest Brazilian customer was 22.0% of its 2024 revenue,\[8\] ≈ RMB 760M ≈ US$105M. At an assumed US$90–150 ex-works ASP, that implies **~0.7–1.2M Android units/year to one Brazilian acquirer** (derived, low confidence).
  - **Derived estimate:** Android smart POS at ~25–35% of Brazil's 35M+ terminals (~9–12M units). Confidence: low.
- **Mexico (LatAm context):** Mercado Pago Point Smart 2 lists at MXN 4,499 but sells for MXN 549 (Amazon MX MXN 399), refundable after MXN 30,000 in processed sales, with no monthly rent.\[15\]\[16\]\[17\]\[59\] It is the archetypal subsidized smart handheld.
- **Argentina, Colombia, Chile, Peru:** no 2024–26 device-level data were captured in this research. Treat these as lower-penetration markets led by acquirers and wallets (Mercado Pago, Fiserv/Posnet, Transbank, Niubiz/Izipay, Bold), with dynamics similar to Brazil and Mexico. Unverified.

### Regional Summary Matrix

| Region | Penetration signal (date) | Dominant form factors | Typical hardware price | Installed base: smart/tablet POS (estimate) | Leading vendors/platforms |
|---|---|---|---|---|---|
| North America | Universal card acceptance; Toast 180k locations (Q2 2026) | Dual-screen AIO, iPad + stand, rugged handhelds, kiosks | $399 handheld; $899–$1,895 countertop; $149 iPad stand | ~8–14M incl. iPads (low conf.) | Toast, Square, Clover; PAX/Ingenico/Verifone for ISVs; Sunmi/iMin via resellers |
| Japan | 42.8% (2024, old metric) → 58.0% (2025, new metric) | Acquirer Android terminals (7"+4" with printer), iPad POS | iPad ¥58,800+; terminal acquirer-bundled | ~0.8–1.2M Android payment + ~0.6–1.0M iPad POS (med-low) | Panasonic/stera (SMBC), PAX, Square, Airレジ, Smaregi |
| Korea | ~3.21M merchants, MDR 0.4–1.45% (2025) | Windows POS + VAN reader; Android front/terminal; kiosks | Not verified | ~0.3–0.6M Android (low); 5.25M total POS (third-party) | Toss Place, POSBANK/OKPOS, VANs (KOVAN, KICC, KIS, NICE) |
| Southeast Asia | QR >> terminals (ID: 42M QRIS vs 2.42M EDC, 2025) | Bank EDCs, Android handhelds, F&B Android AIO | US$249–$599 smart; EDC rented | ~1.3–2.2M Android payment terminals (low–med) | PAX, Sunmi, iMin, banks (BCA, Mandiri, BNI), GHL/StoreHub (not verified) |
| South America | Brazil 35M+ POS (2024); Pix 34% of in-store value | Subsidized Android/Linux handhelds with printer | Mexico Point Smart 2 MXN 399–549 | Brazil ~9–12M Android (low) | Sunmi, PAX, Ingenico, Gertec (not verified); Stone, PagBank, Cielo, Rede, Getnet, Mercado Pago, InfinitePay |

## Hardware and Market Trends / Outlook to 2027–2028

1. **Android to roughly 55–60% of shipments by 2028** (interpolated from Counterpoint's 48% in 2025 and 70% in 2032). Proprietary-OS lines will go into maintenance mode.
2. **Security baseline moves to PCI PTS POI v7.x + EMVCo C-8.** PAX already has A920Pro certified, and Clover moved from PTS 5.x to 6.x between Duo 1 and Duo 2.\[4\]\[31\] Plan for 7.x on every new SKU and C-8 kernel readiness for contactless.
3. **SoC tiering:**
   - Entry 7" payment tablets still ship on Helio P22-class silicon (PAX A3700) with 2GB RAM.\[38\]\[42\]
   - Flagship AIOs ship on 6nm Qualcomm with 6–8GB (Sunmi T3 Pro Max, Square Register).\[12\]\[26\]
   - The memory price shock since Q4 2025 will compress the mid-tier and push vendors to specify 4GB/64GB more carefully.
4. **Dual-screen and printer integration stay standard on countertops.** A 14–15.6" merchant screen plus a 7–15.6" customer screen and an 80mm printer at 250mm/s is the norm.\[12\]\[27\] Handhelds converge on about 6.2–6.5", IP54–IP65, 24h battery, Wi-Fi 6 and LTE.
5. **SoftPOS/MPoC grows at the low end** (stera tap, Tap to Pay). Counterpoint expects it not to displace attended and unattended terminals.\[1\] PM response: make dedicated devices earn their keep with printer, scanner, ruggedness and fleet management.
6. **Real-time QR/A2A rails (Pix, QRIS, DuitNow, PayPay) cap dedicated-terminal demand among micro-merchants.** Smart terminals still win when they render dynamic QR, NFC Pix/QRIS Tap and cards on one device.
7. **Supply chain:**
   - PAX and Sunmi are now both listed in Hong Kong, alongside Centerm/Newland/Landi.
   - Tariff exposure is real: Toast booked a ~$10M tariff refund in Q2 2026, and PAX cites "evolving U.S. terminal deployment & softer demand."\[11\]\[62\]
   - Expect more ASEAN/Mexico final assembly (iMin Johor plant) for US-bound devices.

## Recommendations (for a hardware PM)
1. **Build one Android 13/14 platform with three SKUs:** a 6.5" IP65 handheld with LTE and printer option; a 7–8" PCI PTS 7.x customer tablet with pogo dock; and a 15.6" + 10.1"/15.6" countertop with 80mm printer. Share board, OS and TMS across all three.
2. **Specify memory defensively.** Use 4GB/64GB as the volume configuration, keep 6–8GB for flagship, and dual-source LPDDR/eMMC/UFS.
3. **Price for the channel, not the merchant.** North America: ≤$400 handheld and ≤$900 dual-screen to match Square. Brazil/Mexico: an acquirer BOM target well under US$150 for handhelds. Japan/Korea: certification and local-payment integration (FeliCa, VAN) beat price.
4. **Make the TMS/app store the product.** Use MAXSTORE-scale fleet management as the benchmark, and monetize apps, OTA updates and device analytics.
5. **Regional go-to-market:** in North America, partner with ISVs and processors; in Japan, sell through acquirers (stera-style) and iPad-POS peripherals; in Korea, through VAN/PG-certified bundles with kiosk mode; in Southeast Asia, through bank EDC refresh (Android APOS) and F&B chain AIOs; in Brazil, Mexico and LatAm, through acquirer/wallet subsidized handhelds with dynamic Pix/QR plus NFC.

## Methodology, Assumptions and Confidence
- **Verified figures:**
  - Company filings and press releases: Toast 8-K, PAX annual results, StoneCo 20-F, Sunmi prospectus via press.
  - Regulators and central banks: METI, Bank Indonesia, BSP, BNM, Bank of Thailand/Visa, the FSC via secondary reporting.
  - Industry bodies: ABECS.
  - Analyst firms: Counterpoint, Berg Insight, IHL.
  - Official product pages and authorized resellers.
- **Derived estimates** are explicitly labeled and use location-count × devices-per-site, terminal-count × smart-share, or revenue ÷ ASP methods. All have low or medium-low confidence, because no public source reports smart/tablet POS installed base by country.
- **Data conflicts:**
  - Japan's 42.8% vs 58.0% reflects a METI metric change, not real growth.\[73\]
  - PAX's MAXSTORE count is 16M+ in the annual results vs 18M+ on its website.\[4\]\[5\]
  - Cielo/Rede shares come from lower-quality secondary sites.
  - Market-research revenue sizes for "Android POS" vary wildly (US$3.5bn to US$15bn for 2025)\[105\]\[106\] and were not used.
- **Unverified items:** detailed specs for Verifone, Ingenico, iMin, Castles, Newland, Elo, Zebra, Samsung, Shopify and Stripe devices. Andean/Southern Cone device counts. Singapore terminal counts. Official Toast hardware prices.

## Caveats
- Several prices come from third-party resellers and fluctuate with promotions. Platform list prices (Square, Mercado Pago) are the most reliable.
- Third-party market-sizing reports (Ken Research, Coherent, Statista) are directional only.
- Sunmi's H1 2026 regional split and Vietnam's 2025 POS growth come through secondary outlets.
- The Toast product-page image may be a generic brand image rather than a Toast Go 3 photo.

## 資料來源

1. [Android Nears Half of POS Shipments in a Market That Grew Just 1% in 2025](https://counterpointresearch.com/en/insights/android-nears-half-of-pos-shipments-in-a-market-that-grew-just-1-percent-in-2025)
2. [www.businesswire.com](https://www.businesswire.com/news/home/20250428903740/en)
3. [PAX GLOBAL TECHNOLOGY LIMITED 百富環球科技有限 ...](https://newsfile.moomoo.com/public/NN-PersistNoticeAttachment/7781/20260319/12059440-0.PDF)
4. [PAX Global Announces 2025 Annual Results](https://www.pax.com.cn/PAX-Global-Announces-2025-Annual-Results/)
5. [About Us丨Follow Us丨PAX Global](https://www.pax.com.cn/AboutUs/)
6. [IPO: Global Android-based BIoT Leader SUNMI Technology Lists in Hong Kong](https://www.usmart66.com/en/news-detail/1/7452176115025739860)
7. [【新股IPO】商米科技6810招股集資10.6億元、BIoT解決方案商 入場費2511元|香港經濟日報](https://inews.hket.com/article/4116776/sunmi-6810-ipo-2026)
8. [SUNMI TECH-W's Hong Kong IPO Faces Valuation and Structural Hurdles - Tiger Brokers](https://www.itiger.com/news/1128456168)
9. [三井住友カードがnext steraで決済端末100万台の設置を目指す モバイル、セルフやKIOSK、COTS、DXソリューション等を投入へ](https://paymentnavi.com/paymentnews/142949.html)
10. [三井住友カードがAndroid決済端末stera terminal発表、アプリで決済手段追加](https://xtech.nikkei.com/atcl/nxt/news/18/06112/)
11. [PAX Global Technology Limited (327.HK) 2025 Annual Results](https://uploads.strikinglycdn.com/files/2813b5a1-0b18-4287-a6f0-9a442dc77097/2025-annual-results-presentation_en.pdf)
12. [Sunmi T3 Pro Max Smart Touch POS](https://www.ics.gr/en/sunmi-t3-pro-max-smart-touch-pos)
13. [Register POS System](https://squareup.com/us/en/hardware/register)
14. [Clover Station Duo 2](https://www.limelightpayments.com/store/p/clover-station-duo)
15. [Terminal Point Smart 2: Con Internet Gratis](https://www.mercadopago.com.mx/herramientas-para-vender/lectores-point/point-smart)
16. [Terminal de punto de venta Point Mercado Pago](https://www.mercadopago.com.mx/herramientas-para-vender/lectores-point)
17. [Point Smart 2](https://www.mercadopago.com.mx/herramientas-para-vender/lectores-point/point-smart?code=POINT_ORG&channel=ORGANIC)
18. [PagSeguro Digital Ltd. (NYSE: PAGS) — A Digital Bank Priced as a Dying Acquirer, Bought Back Below Book](https://www.factorstoday.com/research/PAGS)
19. [2024 Ratio of Cashless Payment Among the Total Amount Paid by Consumers Calculated/METI Ministry of Economy, Trade and Industry](https://www.meti.go.jp/english/press/2025/0331_001.html)
20. [2025 Ratio of Cashless Payment Among the Total Amount Paid by Consumers Calculated/METI Ministry of Economy, Trade and Industry](https://www.meti.go.jp/english/press/2026/0331_005.html)
21. [South Korea Payments: Local PGs & Wallets — PaymentBrief](https://paymentbrief.com/articles/south-korea-payments-operator-guide/)
22. [How to Pay in Korea: Complete 2025 Guide to Payment Methods, Cards, and Cash - Korea Navigator](https://koreanavigator.com/how-to-pay-in-korea-2025-guide-to-payment/)
23. <https://www.bi.go.id/id/statistik/ekonomi-keuangan/spip/Documents/TABEL_5f.pdf>
24. [BI unveils cross-border expansion and merchant growth plans for QRIS](https://www.marketing-interactive.com/bi-unveils-cross-border-expansion-and-merchant-growth-plans-for-qris)
25. [Sunmi T3 Pro Max Desktop Terminal P01250004](https://www.thebarcodewarehouse.co.uk/shop/sunmi/desktop-products/sunmi-p01250004/)
26. [2D Sunmi T3 PRO MAX Sunmi](https://www.etiden.com/EN/sunmi-t3-pro-max-sunmi.html)
27. [Sunmi T3 PRO MAX](https://www.sunmi.cz/en/sunmi-t3-pro-max.html)
28. [SUNMI T3 Pro Max POS Terminal 15.6 FHD NFC WiFi GMS 6GB 128GB](https://allstarterminals.com/products/sunmi-t3-pro-max-smart-desktop-terminal-15-6-fhd-80mm-printer-nfc-wifi-6gb-128gb-gms-supported)
29. [SUNMI T3 PRO MAX 15.6" TOUCHSCREEN P01240004](https://www.tech-america.com/item/sunmi-t3-pro-max-15-6-touchscreen-fhd-pos-terminal/p01240004)
30. [Complete SUNMI T3 comparison](https://blog.rospertech.com/sunmi-t3-comparison/)
31. [© 2023 Clover Network Clover Station Duo 2: What’s New Launching June 2023](https://www.merchantindustry.com/wp-content/uploads/2023/12/Clover-Station-Duo-2-Specifications-012024.pdf)
32. [Clover devices—Technical specifications](https://docs.clover.com/dev/docs/clover-devices-tech-specs)
33. [Clover Station Duo + Flex POS Bundle](https://www.limelightpayments.com/store/p/clover-duo-2-clover-flex-3-combo)
34. [Clover Station Duo 2 Bundle POS System - PaymentCloud Shop](https://paymentcloudinc.com/shop/clover/station-duo/)
35. [Restaurant & Bar POS System](https://www.limelightpayments.com/store/p/restaurant-bar-clover-station-duo)
36. [Square hardware: Compare POS devices & pricing](https://fitsmallbusiness.com/square-hardware-comparison/)
37. [Square Processing Fees, Plans, and Software Pricing](https://squareup.com/au/en/pricing)
38. [PAX A3700](https://docs.finix.com/guides/in-person-payments/select-your-device/pax-a3700)
39. [PAX Elys A3700 Customer-Facing Payment Tablet](https://pos.infor.com/products/pax-elys-tablet-a3700-customer-facing-payment-tablet-android-touchscreen)
40. [PAX A3700 丨Elys Tablet](https://www.orderpin.co/hardware/pax-a3700/)
41. [PAX A3700](https://buy.posportal.com/pax-a3700-4g-wi-fi-bluetooth-tablet.html)
42. [PAX A3700 - Geekbench](https://browser.geekbench.com/v4/compute/5235516)
43. [PAX A3700](https://www.ucp-inc.com/product-page/pax-a3700-elys)
44. [stera terminal - どんなシーンでの決済もDXもこの一台で｜stera（ステラ）｜ご加盟店契約、アクワイアラーならクレジットカードの三井住友カード](https://www.smbc-card.com/kamei/stera/terminal/index.jsp)
45. [stera terminal（ステラターミナル）とは？｜stera developers by三井住友カード](https://www.smbc-card.com/steradevelopers/start/terminal.jsp)
46. [三井住友カード、次世代steraを発表 新端末や中小事業者強化 - Impress Watch](https://www.watch.impress.co.jp/docs/news/1578905.html)
47. [stera terminal（ステラ端末）はどこで申し込むのが一番お得？](https://cashless-professional.com/sterahikaku/dounyu/)
48. [Toast POS Pricing 2026: Complete Cost Guide & Hidden Fees Revealed](https://restaunax.com/blog/toast-pos-pricing)
49. [New Toast Go® 3 Handheld with Cellular Connectivity and ToastIQ Unlocks Additional Revenue Potential—Anywhere Restaurants Operate](https://finance.yahoo.com/news/toast-3-handheld-cellular-connectivity-120000107.html)
50. [Toast Launches Toast Go® 3 Handheld Point-of-Sale Device Globally](https://www.morningstar.com/news/business-wire/20260428620893/toast-launches-toast-go-3-handheld-point-of-sale-device-globally)
51. [Toast Go® 3 Handheld Dimensions](https://support.toasttab.com/en/article/Toast-Go-3-Handheld-Dimensions)
52. [Toast Go® 3](https://pos.toasttab.com/hardware/toast-go)
53. [New Toast Go® 3 Handheld with Cellular Connectivity and ToastIQ Unlocks Additional Revenue Potential—Anywhere Restaurants Operate](https://pos.toasttab.com/news/new-toast-go-3-handheld-with-cellular-connectivity-toastiq)
54. [Introducing Square Handheld: A Pocketable Powerhouse to Serve Tables, Manage Inventory, and Close Sales Anywhere](https://seekingalpha.com/pr/20101736-introducing-square-handheld-a-pocketable-powerhouse-to-serve-tables-manage-inventory-and)
55. [Introducing Square Handheld: A Pocketable Powerhouse to Serve Tables, Manage Inventory, and Close Sales Anywhere](https://squareup.com/us/en/press/square-handheld)
56. [Your Next Coffee Run Might Feel Faster. Here’s Why - Techlicious](https://www.techlicious.com/blog/square-launches-square-handheld-pos/)
57. [Square launches new handheld POS device](https://www.drinksindustryireland.ie/square-launches-new-handheld-pos-device/)
58. [PAX Global lifts 2025 profit and expands Android payment terminal lineup - The Globe and Mail](https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/860805/pax-global-lifts-2025-profit-and-expands-android-payment-terminal-lineup/)
59. [MERCADO PAGO POINT Smart 2, Terminal para Tarjetas con Internet Gratis : Amazon.com.mx: Electrónicos](https://www.amazon.com.mx/MERCADO-PAGO-POINT-Terminal-Tarjetas/dp/B0DFK5G31R)
60. [New Toast Go® 3 Handheld with Cellular Connectivity and ToastIQ Unlocks Additional Revenue Potential—Anywhere Restaurants Operate](https://www.businesswire.com/news/home/20250731400794/en/New-Toast-Go-3-Handheld-with-Cellular-Connectivity-and-ToastIQ-Unlocks-Additional-Revenue-PotentialAnywhere-Restaurants-Operate)
61. [Toast, Inc. - Form 8-K - FY2025](https://www.sec.gov/Archives/edgar/data/1650164/000165016425000175/tost-20250331xexhibit991.htm)
62. [Document](https://www.sec.gov/Archives/edgar/data/0001650164/000165016426000162/tost-20260630xexhibit991.htm)
63. [토스플레이스, 결제 단말기 가맹점 수 10만개 돌파 - 파이낸셜뉴스](https://www.fnnews.com/news/202502240828579732)
64. [PAX Global Announces 2025 Annual Results](https://www.paxtech.com.au/en/about-pax/latest-news/pax-global-announces-2025-annual-results/)
65. [토스플레이스, 단말기 출시 2년 만에 가맹점 수 10만개 돌파](https://www.asiae.co.kr/article/2025022408495994867)
66. [PAX Global Announces 2025 Interim Results August 18, 2025](https://uploads.strikinglycdn.com/files/d5421b54-50cf-4337-816f-c9cf73b0a747/PAX%20Global%20Interim%20Financial%20Results%202025.pdf)
67. [Korea Payment Guide: T-money, WOWPASS, and the Card You Cannot Tap](https://www.epickor.com/blog/201)
68. [三井住友カード、Androidスマホが決済端末になる「stera tap」 手数料2.7% - Impress Watch](https://www.watch.impress.co.jp/docs/news/1578831.html)
69. [Toast, Inc. - Form 8-K - FY2026](https://www.sec.gov/Archives/edgar/data/1650164/000165016426000050/tost-20251231xexhibit991.htm)
70. [Payment Devices Market Size, Share and Forecast, 2025-2032](https://www.coherentmarketinsights.com/industry-reports/payment-devices-market)
71. [Square POS Review: Features, Hardware and Pricing](https://www.expertmarket.com/pos/square-review)
72. [Clover Station Duo 2](https://www.limelightpayments.com/store/p/retail-pos-clover-station-duo)
73. [The truth behind the '58% achievement' in the cashless payment ratio: It was just a change in metrics｜Openwave](https://note.com/openwave/n/n91f60fbce623?hl=en)
74. [Mapped: Countries Where Cash Is Still King - Macro Discovery](https://www.macrodiscovery.com/countries-where-cash-is-still-king/)
75. [パナソニックコネクトの決済端末の展開やターミナル市場への見解は？](https://paymentnavi.com/paymentnews/145616.html)
76. [POSレジのシェアはどれくらい？【おすすめのPOSレジや人気メーカーを解説】](https://store.cloudil.jp/pos-regi-share/)
77. [POSレジのシェア率ランキングTOP3｜国内上位メーカーとタブレットPOSの導入数を比較 - Bizcan](https://bizcan.jp/column/posregi-share/)
78. [スマレジとAirレジのシェアはどのくらい？導入実績の比較と数字の読み方](https://www.kurafuji-hd.co.jp/pos-cash-register/smaregi-airregi-share/)
79. [スマレジとAirレジ(エアレジ)の違いを徹底比較【シェアや手数料の違いは？】](https://store.cloudil.jp/smaregi-airregi-compare/)
80. [PAX Global Technology Announces 2025 Annual Results (HKEX:327)](https://6ix.com/news/pax-global-technology-announces-2025-annual-results)
81. [KOVAN :: Korea VAN Service Co.,Ltd.](https://www.kovan.com/?p=cmV0a0tpdGs%3D)
82. [토스플레이스, 가맹점 수 10만개 돌파했다 - 전자신문](https://www.etnews.com/20250224000079)
83. [토스플레이스, 2년 만에 가맹점 10만 곳 돌파](https://www.smarttoday.co.kr/ko-kr/articles/73385)
84. [토스플레이스, 가맹점 수 10만개 돌파…단말기 출시 2년 만 성과 : 네이트 뉴스](https://m.news.nate.com/view/20250224n05830?mid=m02)
85. [South Korea POS Terminal Market Share, Companies & Trends Report 2025-2031](https://www.kenresearch.com/south-korea-pos-terminal-market)
86. [Thailands Digital Payment System Robust: 900,000 EDC Machines, Over One Million QR Points, Foreign Card Spending Hits 300 Billion Baht](https://en.thairath.co.th/money/tech_innovation/tech_companies/2904139)
87. [Collaborative Insights: Bank of Thailand and Visa Chart the Course for Thailand’s Travel and Payment Industries](https://www.visa.co.th/en_TH/about-visa/newsroom/press-releases/collaborative-insights-bank-of-thailand-and-visa-chart-the-course-for-thailands-travel-and-payment-industries.html)
88. [Malaysia's experience in advancing e-payment adoption](https://www.comcec.org/wp-content/uploads/2024/09/4-Malaysia.pdf)
89. [18.4 Billion Transactions Later, How Close Is Malaysia to a Cashless Future?](https://fintechnews.my/57514/payments-remittance-malaysia/bank-negara-malaysia-bnm-report-payments-cashless-digital-transactions/)
90. [2025 report on e-payments measurement MOMENTUM IN MOMENTUM IN MOTION MOTION](https://www.bsp.gov.ph/PaymentAndSettlement/2025_Report_on_E-payments_Measurement.pdf)
91. [Vietnam Number of Terminal: POS, EFTPOS, EDC](https://www.ceicdata.com/en/vietnam/payment-terminal-statistics/no-of-terminal-pos-eftpos-edc)
92. [Vietnam Digital Payments Statistics 2026 — E-Wallets, QR, Mobile & Gateway Data](https://vnmarketinsights.com/stats/vietnam-digital-payments-2026/)
93. [Transaksi Mesin EDC Perbankan Terus Tumbuh hingga Akhir Februari 2025](https://keuangan.kontan.co.id/news/transaksi-mesin-edc-perbankan-terus-tumbuh-hingga-akhir-februari-2025)
94. [Transaksi Melalui Mesin EDC Meningkat Pesat di Awal Tahun 2024](https://keuangan.kontan.co.id/news/transaksi-melalui-mesin-edc-meningkat-pesat-di-awal-tahun-2024)
95. [商米科技2026年上半年营收17.6亿：同比增26%\_凤凰网](https://i.ifeng.com/c/8w5C8DLftLq)
96. [iMin Success Stories](https://www.imin.com/success-stories/)
97. [Singapore-Based iMin Technology Enters Johor, Malaysia With New State-of-the-Art Production Facility - MIDA](https://www.mida.gov.my/media-release/singapore-based-imin-technology-enters-johor-malaysia-with-new-state-of-the-art-production-facility/)
98. [Annual number of POS terminals in Brazil 2012-2024](https://www.statista.com/statistics/1316884/pos-terminal-count-in-brazil/)
99. [StoneCo Ltd. - Form 20-F - FY2025](https://www.sec.gov/Archives/edgar/data/0001745431/000207097926000170/stne-20251231.htm)
100. [Payment methods in Brazil (2026): 30 local methods & 24 providers](https://paymentsdatabase.com/countries/br)
101. [Brazil POS Terminal Market 2026: \$821M](https://www.ihlservices.com/news/analyst-corner/2026/03/brazil-pos-terminal-market-2026/)
102. [CloudWalk revenue, funding & growth rate](https://sacra.com/c/cloudwalk/)
103. [What is Competitive Landscape of Cielo Company?](https://matrixbcg.com/blogs/competitors/cielo)
104. [What is Brief History of Cielo Company?](https://matrixbcg.com/blogs/brief-history/cielo)
105. [Android POS Market 2026 to 2034](https://www.intelmarketresearch.com/android-pos-market-market-market-15304)
106. [Android POS Terminals Market Research Report 2034](https://dataintelo.com/report/android-pos-terminals-market)