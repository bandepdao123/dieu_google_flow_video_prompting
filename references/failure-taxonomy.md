# Flow generation failure taxonomy

## Identity and continuity
- `identity_drift`
- `age_or_face_drift`
- `hair_drift`
- `wardrobe_drift`
- `accessory_drift`
- `environment_layout_drift`
- `weather_or_time_drift`
- `lighting_direction_drift`
- `prop_geometry_drift`
- `prop_state_or_handedness_error`
- `screen_direction_flip`
- `state_handoff_failure`

## Motion and camera
- `motion_too_weak`
- `motion_too_fast`
- `physics_failure`
- `hand_object_interaction_failure`
- `camera_misread`
- `camera_conflict`
- `transition_failure`
- `prompt_overload`

## Style and audio
- `style_drift`
- `palette_texture_drift`
- `dialogue_timing`
- `lip_sync_issue`
- `audio_source_mismatch`
- `ambience_or_music_conflict`

## Graphics and extras
- `extra_subject`
- `text_or_logo_error`
- `unwanted_object`

## Revision method

For every observed failure record:
- expected result;
- observed evidence;
- likely cause: prompt, asset conflict, overload or model variance;
- elements to preserve;
- one controlled change;
- revised prompt;
- post-revision result if tested.

Do not convert an untested hypothesis into a permanent rule.