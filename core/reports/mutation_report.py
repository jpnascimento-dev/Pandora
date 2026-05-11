class MutationReport:
    def __init__(self):
        self.entries = []

    def add_entry(self, mutation_type, original, new, line):
        self.entries.append({
            "type": mutation_type,
            "original": original,
            "new": new,
            "line": line
        })

    def show(self):
        for entry in self.entries:
            print("\nMutation Applied")
            print("----------------")
            print(f"Type: {entry['type']}")
            print(f"Original: {entry['original']}")
            print(f"New: {entry['new']}")
            print(f"Line: {entry['line']}")