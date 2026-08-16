# Flow multi-reference / ingredients continuity

## Asset assignment
- Asset 1 → `CHAR_A` identity only.
- Asset 2 → wardrobe/product geometry.
- Asset 3 → `LOC_01` layout/environment.
- Asset 4 → style, palette and lighting only.

Replace with actual roles. Explicitly state what must not be borrowed from each style-only asset.

## Prompt

```text
Use the provided references with these roles: [role map]. Keep [CHAR_A canonical identity], [exact wardrobe], [PROP state] and [LOC_01 spatial layout] unchanged. [Shot composition]. [Action chronology]. The camera [one coherent move]. Preserve [time/weather/light direction/palette/lens family]. [Audio]. End with [handoff].
```

## Cross-clip locks
- Canonical identity phrase:
- Location landmarks:
- Prop holder/state:
- Screen direction:
- Lighting source/direction:

## Risk check
Conflicting references require one master; do not average incompatible faces, wardrobe or architecture.