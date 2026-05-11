import ast
from pathlib import Path

from plugins.python.mutator import ComparisonMutator

source_path = Path("examples/sample.py")

source_code = source_path.read_text()

tree = ast.parse(source_code)

mutator = ComparisonMutator()
mutated_tree = mutator.visit(tree)

mutated_code = ast.unparse(mutated_tree)

output_path = Path("examples/sample_mutated.py")
output_path.write_text(mutated_code)

mutator.engine.report.show()

print(f"\nMutated code written to {output_path}")