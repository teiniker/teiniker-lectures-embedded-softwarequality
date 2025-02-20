# Abstract Syntax Tree


## Python AST Module 

The **ast module** helps Python applications to process trees of the Python abstract syntax grammar.

```
import ast
```

```
tree = ast.parse("value = 1 + 2")
print(ast.dump(tree, indent=4))
```

```
Module(
    body=[
        Assign(
            targets=[
                Name(id='value', ctx=Store())],
            value=BinOp(
                left=Constant(value=1),
                op=Add(),
                right=Constant(value=2)))],
    type_ignores=[])
```


## References
* [ast — Abstract Syntax Trees](https://docs.python.org/3/library/ast.html)

* [Abstract Syntax Trees in Python](https://pybit.es/articles/ast-intro/)

* [YouTube: Python AST Parsing and Custom Linting](https://youtu.be/OjPT15y2EpE)
	
* [YouTube: Chase Stevens - Exploring the Python AST Ecosystem](https://youtu.be/Yq3wTWkoaYY) 
