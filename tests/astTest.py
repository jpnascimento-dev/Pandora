import ast

code = "x = 5"

tree = ast.parse(code)

print(ast.dump(tree, indent=4))