# Script-to-shot and feasibility

## Decomposition

Divide by visual beat, not punctuation. Each clip needs one visual objective, start state, central action, end state, camera logic, emotion and audio job.

## Complexity check

Risk rises with:
- number of subjects and interactions;
- action beats;
- camera transitions;
- complex object/hand contact;
- transformation or difficult physics;
- dialogue load;
- duration pressure.

Default to one central action and one coherent camera move. Split when clarity or continuity would suffer.

## Multi-clip plan

For each clip define:
- `clip_id`;
- narrative function;
- inherited state;
- asset assignment;
- global continuity locks;
- shot action;
- end-state handoff.

## Timestamp usage

Use timestamp prompting only when multiple shots inside one generation are necessary. Segments cannot overlap and must sum to total duration. Give each segment a distinct visual beat while preserving identity, props, environment and progression.

## Dialogue budget

Estimate speech against duration, emotion, pauses and reactions. If uncertain, shorten dialogue or split clips. Do not force long exposition into a short visual clip.

## Repair choices

If overloaded:
1. remove secondary movement;
2. simplify camera;
3. shorten dialogue;
4. use a continuous shot;
5. split into multiple clips and carry state forward.