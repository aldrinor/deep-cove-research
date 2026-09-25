# Results

RACE results for the 100 reports in [`data/deep-cove-research.jsonl`](../data/deep-cove-research.jsonl), from a local run of the official DeepResearch Bench RACE evaluation code (commit `852f4022`, default evaluator settings). Scores are on the 0–100 scale.

## race_scores.json

| Field | Content |
|:--|:--|
| `evaluation` | How the scores were produced. |
| `scores` | Overall score and the four dimension scores. |
| `per_task` | The overall score for each task id. |

Score keys: `overall_score`, `comprehensiveness`, `insight`, `instruction_following`, `readability`. The overall score equals the mean of the 100 per-task scores.
