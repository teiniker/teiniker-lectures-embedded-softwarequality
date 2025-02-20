import ast

tree = ast.parse("value = 1 + 2")
print(ast.dump(tree, indent=4))
