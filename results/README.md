# Results

RACE results for the 100 reports in [`data/deep-cove-research.jsonl`](../data/deep-cove-research.jsonl), from a local run of the official DeepResearch Bench RACE evaluation code (commit `852f4022`, default evaluator settings). Official verification is pending. Scores are on the 0–100 scale.

## race_scores.json

| Field | Content |
|:--|:--|
| `evaluation` | How the scores were produced. |
| `single_pass` | Overall score and the four dimension scores for the official pipeline run once. |
| `verified_cleaning` | The same, with the official cleaning step re-run for the 10 tasks that carry `recleaned_*` fields in `cleaning_evidence.json`. |
| `per_task` | For each task id: the overall score in both evaluations (`single_pass`, `verified_cleaning`). |

Score keys: `overall_score`, `comprehensiveness`, `insight`, `instruction_following`, `readability`. The overall score equals the mean of the 100 per-task scores.

## cleaning_evidence.json

One entry per task, in task order.

| Field | Content |
|:--|:--|
| `task` | Task id. |
| `raw_chars` | Length of the report in Unicode characters. |
| `cleaned_chars` | Length of the text returned by the official cleaning step in the single pass. |
| `kept` | `cleaned_chars / raw_chars`, rounded to three decimals. |
| `official_score` | The task's overall score in the single pass (equal to `per_task.single_pass`). |
| `recleaned_kept` | Only for the 10 re-run tasks: the kept share when the cleaning step was run again. |
| `recleaned_score` | Only for those tasks: the overall score with the re-run (equal to `per_task.verified_cleaning`). |
