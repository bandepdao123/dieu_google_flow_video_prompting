# Continuity System

## Master principle

Consistency is created by combining approved reference assets, stable wording, scene-state tracking and controlled variation. Repeating prose alone cannot guarantee identity.

## Lock levels

- **HARD**: identity, approved wardrobe, product geometry, persistent location layout, critical prop state. Never change without approval/story transition.
- **SOFT**: expression, pose, camera distance, local light intensity; change only when the beat calls for it.
- **FREE**: minor background motion, incidental particles, nonessential extras.

## Character master

Record:
- stable ID, e.g. `CHAR_A`;
- master reference asset(s);
- face geometry and visible anchors;
- hair style/color/length;
- apparent age, skin, build, height relationship;
- exact wardrobe and accessories by scene;
- body-language signature;
- voice/accent/delivery;
- forbidden drift.

Use one short canonical identity phrase verbatim across clips. Do not invent new facial details after clip 1.

## Environment master

Record:
- stable ID, e.g. `LOC_01`;
- layout and spatial landmarks;
- surfaces/materials;
- doors/windows/large props and relative positions;
- time, weather and atmosphere;
- key-light source and direction;
- palette/contrast/texture;
- camera axis and screen geography.

For angle changes, describe where camera and character are relative to landmarks. Preserve the 180-degree axis unless an intentional crossing shot is specified.

## Prop/product ledger

For every persistent object:
- ID and master asset;
- geometry/material/color;
- size relative to hand/body;
- orientation and position;
- holder and which hand;
- state before/after each clip.

## State handoff

Every connected clip stores:
- character position and pose;
- gaze direction;
- movement direction;
- emotion;
- prop holder/state;
- environment changes;
- camera end position;
- audio tail.

The next clip inherits these before adding a new action. Use the actual end frame as the next reference when Flow workflow permits.

## Controlled change protocol

Any planned continuity change must specify:
1. current state;
2. trigger/action;
3. new state;
4. elements that remain unchanged.

Examples: wardrobe change, day-to-night, object opens/breaks, character becomes wet/dirty/injured.

## Cross-shot audit

Before delivery compare adjacent clips for:
- same identity anchors;
- wardrobe/accessories;
- handedness and prop state;
- location layout and weather;
- light direction and palette;
- movement/screen direction;
- emotional progression;
- beginning state equals prior ending state.

If any mismatch is not story-motivated, repair the prompt or asset assignment.