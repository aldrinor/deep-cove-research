# deep-cove-research

deep-cove-research is a proprietary deep-research system. For each question it:

1. plans the research: what must be answered and how the report should be structured;
2. searches the open web and the scholarly literature;
3. reads the full text of the selected sources;
4. extracts cited findings from them;
5. checks coverage against the question's requirements;
6. writes a long-form report.

The reports are written by the **GPT-5.6 Luna** model at its maximum reasoning setting.

## DeepResearch Bench results

The 100 reports (50 Chinese, 50 English) were evaluated with the official DeepResearch Bench RACE evaluation code
(commit 852f4022), using its default evaluator settings.

| Evaluation | Overall | Comprehensiveness | Insight | Instruction Following | Readability |
|---|---|---|---|---|---|
| Official pipeline, cleaned reports verified | **55.23** | 55.80 | 55.92 | 55.23 | 52.26 |
| Official pipeline, single pass | 54.81 | 55.25 | 55.48 | 54.85 | 52.10 |

**Note on the cleaning step.** Before judging, the official pipeline asks a model to remove citations from each report.
- In the single pass, that step returned only the opening part of 10 long Chinese reports (for example, 11% of task 19),
  and the pipeline accepted those outputs.
- Re-running the cleaning step for those 10 reports gave complete outputs. That is the "verified" row.
- Per-task cleaned lengths and scores are in `results/`.

## Files

- `data/deep-cove-research.jsonl`: the 100 raw reports in the official format (`id`, `prompt`, `article`).
- `results/race_scores.json`: overall and per-task scores for both evaluations.
- `results/cleaning_evidence.json`: per-task raw and cleaned lengths from the official cleaning step.

## License

Proprietary. The system's source code is not released.
