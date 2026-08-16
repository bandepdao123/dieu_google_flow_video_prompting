# Optional API notes — not part of normal Flow workflow

The production destination for this skill is Google Flow. Do not show API guidance unless Sếp explicitly requests automation or developer integration.

The Google Omni document verified 2026-08-14 described `gemini-omni-flash-preview`, Interactions API, text/image/reference/edit tasks and stateful editing. These details can change because the model was preview. Re-fetch official docs before any implementation.

Never mix Gemini Omni Interactions API request schemas with Veo/Vertex prediction schemas, and never assume a documented API feature appears as a control in the current Google Flow UI.