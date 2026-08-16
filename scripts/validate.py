#!/usr/bin/env python3
"""Lean, dependency-free repository and fixture validator."""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def fail(msg): errors.append(msg)

skill = (ROOT / "SKILL.md").read_text()
if not re.search(r"^name: dieu_google_flow_video_prompting$", skill, re.M): fail("skill name changed")
if not re.search(r"^version: 2\.1\.0$", skill, re.M): fail("version must be 2.1.0")
for required in ("compact", "standard", "production", "workflow-router.md", "language-policy.md"):
    if required not in skill: fail(f"SKILL.md missing {required}")

for path in sorted((ROOT / "templates").glob("*.md")):
    text = path.read_text()
    for i, block in enumerate(re.findall(r"```text\n(.*?)\n```", text, re.S), 1):
        if len(block.splitlines()) != 1 or not block.strip(): fail(f"{path.name} prompt block {i} is not one physical paragraph")

bible = (ROOT / "assets/continuity-bible.yaml").read_text()
for key in ("asset_registry:", "nine_layers:", "START:", "CHANGE:", "END:", "HANDOFF:", "prop_state:", "camera_state:", "audio_state:"):
    if key not in bible: fail(f"continuity bible missing {key}")

fixtures = ROOT / "evals" / "fixtures.json"
if not fixtures.exists(): fail("missing eval fixtures")
else:
    data = json.loads(fixtures.read_text())
    for case in data:
        expected = case.get("expected", {})
        if expected.get("temporal_causality") == "hard_fail" and not case.get("input", {}).get("causality_conflict"):
            fail(f"fixture {case.get('id')} hard-fail lacks conflict")

if errors:
    print("FAIL")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"PASS: repository contract, {len(list((ROOT/'templates').glob('*.md')))} templates validated")
