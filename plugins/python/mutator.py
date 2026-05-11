import ast

from core.engine.mutation_engine import MutationEngine


class ComparisonMutator(ast.NodeTransformer):
    def __init__(self):
        self.engine = MutationEngine()

    def visit_Compare(self, node):
        self.generic_visit(node)

        node = self.engine.apply(node)

        return node