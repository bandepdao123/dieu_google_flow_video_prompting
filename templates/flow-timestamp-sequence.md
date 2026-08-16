# Flow timestamp sequence

Use only when multiple shots inside one generation are necessary.

## Global locks
Character identity, wardrobe, props, location, lighting and palette apply to every segment.

```text
[00:00-00:02] [shot/action]. End state: [...].
[00:02-00:04] Begin from the prior end state. [shot/action + SFX]. End state: [...].
[00:04-00:06] Begin from the prior end state. [shot/action]. End state: [...].
[00:06-00:08] Begin from the prior end state. [final shot/action + audio].
```

Segments cannot overlap and must total duration. Keep screen direction, prop state and emotional progression coherent.