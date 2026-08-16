# Google Flow QA and hard fails

## Weighted QA (100)

- Input fidelity: 15
- Character consistency: 20
- Environment/prop continuity: 20
- Temporal handoff: 15
- Shot feasibility and camera logic: 10
- Style/lighting consistency: 10
- Audio coherence: 5
- Flow copy-readiness: 5

Target: 85+. Any hard fail overrides score.

## Hard fails

Do not deliver until repaired:
- prompt contradicts approved asset or locked fact;
- identity phrase/wardrobe drifts without approved change;
- location layout, weather or light direction changes unintentionally;
- prop changes hand/state/geometry without transition;
- connected clips lack end-state handoff;
- screen direction or camera axis flips unintentionally;
- conflicting camera instructions;
- action/dialogue overloads duration;
- timestamp overlap or wrong total;
- first/last frames lack plausible transition;
- important asset has no assigned role;
- revision lacks Preserve and Change instructions;
- API code/schema appears without request.

## Flow readiness

Confirm:
- prompt is directly copyable;
- assets are named and assigned in upload order;
- prompt distinguishes identity, environment and style references;
- duration/aspect/audio recommendations are visible;
- negative prompt is separate only when usable;
- risk notes are concise and actionable.

## Adjacent clip QA

Compare Clip N end with Clip N+1 start:
- pose/position/gaze;
- movement and screen direction;
- emotion;
- prop holder/state;
- environment/time/weather;
- lighting direction;
- camera geography;
- audio tail.

Repair every unexplained mismatch.