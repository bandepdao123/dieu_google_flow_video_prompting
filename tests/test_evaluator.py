import copy,json,unittest
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
if __name__=="__main__":unittest.main()
