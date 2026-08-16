# Language policy

- Follow the user's requested output language; otherwise use the user's language for management notes.
- Write the copy-ready prompt in the language the user requests. If unspecified, use English for precise visual controls while preserving dialogue verbatim in its intended spoken language.
- Never translate names, visible brand text, quoted dialogue, canonical identity phrases, or normalized IDs unless explicitly requested.
- Declare mixed-language dialogue and pronunciation intent outside the prompt block when useful.
- Keep one terminology set across clips; do not alternate synonyms for locked anchors.
- IDs are ASCII uppercase normalized as `ASSET_001`, `CHAR_A`, `LOC_01`, `PROP_01`, `CLIP_001`; never derive IDs from filenames or mutable prose.
