# Flow first + last frame

## Use
Controlled transition, transformation or camera move between approved states.

## Preflight
- Same character identity and wardrobe unless change is intentional.
- Spatially plausible location/layout.
- Start and end camera geometry can be connected.
- Planned prop/state transformation is explicit.

## Prompt

```text
Begin exactly from the supplied first frame. Preserve [identity, wardrobe, props,
location, palette and lighting anchors]. Over [duration], [chronological transition
path with subject/environment motion]. The camera [coherent movement path].
[Audio progression]. Arrive naturally and precisely at the supplied last frame,
with [final pose, gaze, prop state and camera state].
```

Do not redescribe contradictory details. If the frames conflict, repair assets or seek approval before prompting.