# Data

[`deep-cove-research.jsonl`](deep-cove-research.jsonl) holds the 100 reports, unchanged, in the official DeepResearch Bench format: one JSON object per line, UTF-8.

| Field | Type | Content |
|:--|:--|:--|
| `id` | integer | Task number, 1–100. Tasks 1–50 are Chinese, 51–100 English. |
| `prompt` | string | The benchmark task, unchanged. |
| `article` | string | The report text, with its source links inline. |

- Lines: 100, in `id` order.
- Size: 8,010,129 bytes.
- SHA-256: `2578948bbb4555c30c3dc9c1bc245a59e2c1575f0c2a8fd5c3f7c3ccad3c12e3`

A readable page for every report is in [`reports/`](../reports/README.md).
