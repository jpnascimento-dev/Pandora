import ast
import random

class ComparisonMutation:
    @staticmethod
    def mutate(node, report, mutation_chance):
        replacements = {
            ast.GtE: ">=",
            ast.Lt: "<",
            ast.LtE: "<=",
            ast.Eq: "==",
        }
        
        for i, op in enumerate(node.ops):
            if isinstance(op, ast.Gt):
                
                should_mutate = random.random()
                
                if should_mutate <= mutation_chance:
                
                    new_operator = random.choice(
                        list(replacements.keys())
                    )

                    node.ops[i] = new_operator()
                    
                    report.add_entry(
                        mutation_type = "Comparison Mutation",
                        original = ">",
                        new = replacements[new_operator],
                        line = node.lineno
                    )

        return node