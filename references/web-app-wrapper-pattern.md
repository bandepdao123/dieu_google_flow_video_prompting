# Web App Wrapper Pattern for Flow Prompting

Use this pattern when turning this skill into an internal website with script input, reference-image upload, settings, and copy-ready prompt output.

## Recommended architecture

`Browser UI → authenticated backend → Hermes/model runtime → dieu_google_flow_video_prompting → structured display`

- Keep provider credentials on the backend in environment/local secret storage; never expose them to the browser.
- Preload the skill explicitly when invoking Hermes, e.g. `hermes -s dieu_google_flow_video_prompting chat -q "..."`, rather than relying only on a natural-language request to use it.
- Prefer an API/server integration for production. A spawned CLI process is acceptable for an internal prototype but needs timeout, concurrency, cancellation, error handling, and output parsing.
- Provide a deterministic demo/fallback mode, but label it clearly as template/demo output rather than skill-backed AI output.

## Input contract

Collect:
- script/brief;
- desired or automatic clip count;
- aspect ratio and duration;
- prompt language and visual style;
- reference assets with an explicit role: identity, wardrobe, product, environment, style, start frame, end frame, or motion.

Do not treat filename/MIME/size metadata as visual understanding. If image pixels are not actually passed to a vision-capable model, state that limitation and do not invent image details. For production, send the image content or an authorized stored-object reference through the vision path, then convert observations into Continuity Bible locks.

## Output contract

Return stable fields per clip:
- clip ID and visual objective;
- inherited state;
- asset assignments;
- continuity locks;
- one copy-ready prompt;
- end-state handoff;
- risks/revision note.

The copy-ready prompt must be one continuous paragraph. Multiple prompts must be separated by exactly one blank line. Management labels may remain outside prompts.

## Minimum UX

- Script textarea with validation that preserves input after errors.
- Multi-image upload with previews and per-image role selection.
- Settings for clip count, duration, aspect ratio, workflow/style, and mode.
- Generate, copy-one, copy-all, loading, empty, and actionable error states.
- Clearly distinguish `Demo` from `AI via Hermes`.
- Verify at desktop and mobile widths; do not claim visual QA if browser rendering could not be completed.

## Verification gates

1. Unit test paragraph formatting and exact blank-line separation.
2. Test input limits and empty-script validation.
3. Test health endpoint and one real generation request.
4. Test upload limits and unsupported files.
5. Test Hermes timeout/failure and fallback labeling.
6. For AI mode, verify logs/runtime evidence that the skill was explicitly preloaded.
7. Run browser QA at desktop and mobile; if Chromium sandbox blocks launch, use an installed browser with a controlled `--no-sandbox` container-only fallback or report visual QA as incomplete.

## Common pitfalls

- Saying the website “uses the skill directly” when it only uses a hand-written template.
- Passing `--toolsets skills` but not explicitly preloading the named skill.
- Uploading images to the backend while sending only file metadata to the model.
- Returning free-form text that the UI cannot reliably split into clips; prefer a validated structured response internally, then render human-readable prompts.
- Reporting browser/UI verification as complete after only API and static-file checks.
