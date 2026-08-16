# dieu_google_flow_video_prompting

Production-grade lean skill for turning scripts, briefs, and approved assets into copy-ready Google Flow video prompts with explicit routing and continuity control.

## Guarantees

- Exact skill name and `dieu_` namespace retained.
- Explicit workflow → template routing and compact/standard/production profiles.
- Nine-layer continuity bible with normalized asset/entity IDs and START/CHANGE/END/HANDOFF state.
- Temporal causality hard fails, feasibility and camera hierarchy, language policy, and failure taxonomy.
- Every template prompt block is one physical paragraph. Delivered multiple prompts are separated by exactly one blank line.
- API/web references remain optional; this repository does not automate Flow or APIs.

## Validate

```bash
python3 scripts/validate.py
```

The validator checks metadata, required production contracts, fixture integrity, and physical prompt-paragraph formatting. See `evals/fixtures.json`.

## Use

Load `SKILL.md`, inventory/normalize assets, create the continuity bible, apply `references/workflow-router.md`, fill the selected template, then run hard-fail QA. Management material remains outside the clean copy-ready prompt block.

License: MIT.
