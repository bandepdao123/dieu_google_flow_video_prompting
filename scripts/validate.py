#!/usr/bin/env python3
"""Production-lean repository validator and deterministic eval runner."""
from pathlib import Path
import json,re,sys,yaml
ROOT=Path(__file__).resolve().parents[1]
REQUIRED={"SKILL.md","README.md","CHANGELOG.md","LICENSE","assets/continuity-bible.yaml","evals/fixtures.json","references/workflow-router.md","references/language-policy.md","references/flow-qa-hard-fails.md"}
LINK=re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)|`((?:assets|references|templates|evals)/[^`]+)`")

def evaluate(i):
 if i.get("existing_generation") and (not i.get("preserve",True) or not i.get("change",True)): return {"hard_fail":"revision_contract"}
 if i.get("existing_generation"): return {"workflow":"revision"}
 if i.get("connected_clips",0)>1 and i.get("handoff") is False:return {"hard_fail":"missing_handoff"}
 if i.get("connected_clips",0)>1:return {"profile":"production"}
 if i.get("start_matches_previous_end") is False:return {"hard_fail":"temporal_causality"}
 if len(set(i.get("camera_moves",[])))>1:return {"hard_fail":"camera_contradiction"}
 if i.get("beats",0)>max(2,i.get("duration",8)//3):return {"action":"split_clips"}
 if re.search(r"(?i)api[_ -]?key|json schema",i.get("output","")):return {"hard_fail":"api_leakage"}
 if any("\n" in p or not p.strip() for p in i.get("prompts",[])):return {"hard_fail":"formatting"}
 return {}

def validate(root=ROOT):
 e=[]
 for x in sorted(REQUIRED):
  if not (root/x).is_file():e.append(f"missing {x}")
 try:
  text=(root/"SKILL.md").read_text(); parts=text.split("\n---\n",1)
  if not text.startswith("---\n") or len(parts)!=2:raise ValueError("strict frontmatter delimiters required")
  meta=yaml.safe_load(parts[0][4:])
  if meta.get("name")!="dieu_google_flow_video_prompting":e.append("exact name changed")
  if meta.get("version")!="2.1.0":e.append("version must be 2.1.0")
  if meta.get("author")!="Trump Creative" or meta.get("license")!="MIT":e.append("author/license metadata invalid")
 except Exception as x:e.append(f"SKILL.md: {x}")
 try: yaml.safe_load((root/"assets/continuity-bible.yaml").read_text())
 except Exception as x:e.append(f"invalid asset YAML: {x}")
 templates=sorted((root/"templates").glob("*.md"))
 for p in templates:
  blocks=re.findall(r"```text\n(.*?)\n```",p.read_text(),re.S)
  if len(blocks)!=1 or len(blocks[0].splitlines())!=1 or blocks[0]!=blocks[0].strip():e.append(f"{p.name}: exactly one one-paragraph prompt block required")
 try:
  router=(root/"references/workflow-router.md").read_text()
  routed=set(re.findall(r"`(templates/[^`]+)`",router))
  for target in routed:
   if not (root/target).is_file():e.append(f"router target missing: {target}")
  for template in templates:
   target=template.relative_to(root).as_posix()
   if target not in routed:e.append(f"router missing required template: {target}")
 except OSError:pass
 for p in root.rglob("*.md"):
  for m in LINK.finditer(p.read_text()):
   target=(m.group(1) or m.group(2)).split("#")[0]
   if not target or target.startswith(("http:","https:","mailto:")):continue
   q=(p.parent/target) if m.group(1) else (root/target)
   if not q.exists():e.append(f"broken link: {p.relative_to(root)} -> {target}")
 try:
  cases=json.loads((root/"evals/fixtures.json").read_text()); ids=[c.get("id") for c in cases]
  if len(ids)!=len(set(ids)) or None in ids:e.append("eval IDs must be present and unique")
  for c in cases:
   if evaluate(c["input"])!=c["expected"]:e.append(f"eval mismatch: {c['id']}")
 except Exception as x:e.append(f"eval inventory invalid: {x}")
 return e
if __name__=="__main__":
 e=validate(); print("PASS: repository and executable eval contracts" if not e else "FAIL\n"+"\n".join("- "+x for x in e));sys.exit(bool(e))
