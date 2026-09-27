# Data

[`deep-cove-research.jsonl`](deep-cove-research.jsonl) holds the 100 reports in the official DeepResearch Bench format: one JSON object per line, UTF-8.

| Field | Type | Content |
|:--|:--|:--|
| `id` | integer | Task number, 1–100. Tasks 1–50 are Chinese, 51–100 English. |
| `prompt` | string | The benchmark task, unchanged. |
| `article` | string | The report text, with numbered citation markers and a numbered reference list at the end. |

- Lines: 100, in `id` order.
- Size: 7,909,321 bytes.
- SHA-256: `fbb0031f3963d91faed70526f3f8b30ecbf1cd3dae5f92ecff8fb9061484df05`

A readable page for every report is in [`reports/`](../reports/README.md).
