# Explicit workflow → template router

Apply the first matching route; record the reason. Never route from assumed API/UI controls.

- Existing generation to repair → **revision** → `templates/flow-revision-after-generation.md`.
- Script exceeds one feasible clip → **multiple clips** → `templates/flow-script-to-multiple-clips.md`.
- Approved first and last images → **first + last frame** → `templates/flow-first-last-frame.md`.
- Multiple references with distinct roles → **multi-reference** → `templates/flow-multi-reference-continuity.md`.
- Product is the hero → **product commercial** → `templates/flow-product-commercial.md`.
- Spoken interaction is central → **dialogue scene** → `templates/flow-dialogue-scene.md`.
- Multiple indispensable beats must share one generation → **timestamp sequence** → `templates/flow-timestamp-sequence.md`.
- Otherwise → **single/text/image-to-video** → `templates/flow-single-or-image-to-video.md`.

## Profile router

- **compact**: one shot, low risk; workflow, essential assets/locks, prompt, settings, risk.
- **standard** (default): full externally useful output contract in `SKILL.md`.
- **production**: multi-clip, client-critical, or high continuity risk; standard plus complete bible, feasibility ledger, START/CHANGE/END/HANDOFF and scored QA.

Escalate compact → standard for ambiguity or persistent assets; standard → production for connected clips, causal state changes, complex interaction, or conflicting approved inputs.
