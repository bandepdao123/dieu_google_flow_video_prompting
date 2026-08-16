import copy,json,shutil,tempfile,unittest
from pathlib import Path
from scripts.validate import evaluate,validate
ROOT=Path(__file__).resolve().parents[1]
class EvaluatorTests(unittest.TestCase):
 def test_all_cases(self):
  for c in json.loads((ROOT/"evals/fixtures.json").read_text()):
   with self.subTest(c["id"]):self.assertEqual(evaluate(c["input"]),c["expected"])
 def test_mutated_expected_fails(self):
  c=json.loads((ROOT/"evals/fixtures.json").read_text())[0];bad=copy.deepcopy(c["expected"]);bad["workflow"]="wrong"
  self.assertNotEqual(evaluate(c["input"]),bad)
 def test_repository(self):self.assertEqual(validate(),[])
 def test_router_must_reference_every_workflow_template(self):
  with tempfile.TemporaryDirectory() as tmp:
   package=Path(tmp)/"flow";shutil.copytree(ROOT,package,ignore=shutil.ignore_patterns(".git","__pycache__"))
   router=package/"references/workflow-router.md";text=router.read_text()
   router.write_text("\n".join(line for line in text.splitlines() if "flow-dialogue-scene.md" not in line)+"\n")
   self.assertIn("router missing required template: templates/flow-dialogue-scene.md",validate(package))
if __name__=="__main__":unittest.main()
