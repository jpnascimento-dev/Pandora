from plugins.python.mutations.comparison import ComparisonMutation
from core.reports.mutation_report import MutationReport

class MutationEngine:
    def __init__(self, mutation_chance=0.5):
        self.mutations = [
            ComparisonMutation
        ]
        
        self.mutation_chance = mutation_chance
        
        self.report = MutationReport()

    def apply(self, node):
        for mutation in self.mutations:
            node = mutation.mutate(
                node, 
                self.report,
                self.mutation_chance
            )

        return node