# Google official sources — verified 2026-08-14

## Video generation prompt guide
URL: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide
Last updated shown: 2026-08-13 UTC.

- Applies to Gemini Omni Flash and Veo.
- Anatomy includes subject, action, scene/context, cinematography, style/ambiance and audio; not every element is mandatory.
- Specific subject/action language reduces generic output.
- Negative prompt field: list unwanted elements directly; avoid instructive `no/don't` wording.
- Safety filters apply.

## Ultimate prompting guide for Veo 3.1
URL: https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
Published: 2025-10-16.

- Formula: `[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]`.
- Article states 720p/1080p, 16:9/9:16, 4/6/8 seconds and synchronized audio/dialogue; verify current Flow options at execution time.
- Workflows: image-to-video, ingredients/reference, first+last frame and timestamp prompting.
- Audio examples use quoted dialogue, `SFX:` and `Ambient noise:`.
- Veo outputs are SynthID-marked according to the article.

## Gemini Omni Flash
URL: https://ai.google.dev/gemini-api/docs/omni
Last updated shown: 2026-07-30 UTC.

- Native multimodality across text, image, audio and video.
- Generates and edits video with audio.
- High-resolution image input plus explicit subject/camera/environment motion is recommended over vague `make it move`.
- Supports multiple subject-reference images and conversational/stateful editing in its API context.

## Flow usage rule

These sources establish prompting principles and capabilities. The production destination for this skill is Google Flow. Do not output API code or assume UI controls not visible in the current Flow project. When a documented capability is not exposed in Flow, adapt the creative workflow instead of inventing a setting.