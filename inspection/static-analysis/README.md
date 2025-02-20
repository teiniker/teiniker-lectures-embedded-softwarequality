# Static Code Analysis 

Static code analysis is the **process of extracting information about a program** from its artifacts using automatic tools (as shown by the figure from Brian Chess, Jacob West).

![Static Code Analysis](figures/StaticAnalysis.png)

**Static analysis tools** accept code, build a model that represents the program, analyze that model in combination with a body of Rules, and finish by presenting their results back to the user.
A static analysis tool **transforms the code into a program model**, a set of data structures that represent the code.

Static analysis tools borrow a lot from the compiler building world: 
* **Lexical Analysis**: By grouping input characters into tokens, a **Lexer** reduces the number of individual items that must be inspected by the parser.
    A Lexer typically:
    * Removes comments.
    * Saves the text of interesting tokens like identifiers, strings, and numeric literals.    
    * Tags tokens with line and column numbers to generate error messages.

* **Syntax Analysis (Parsing)**: A **Parser** calls the lexer to obtain the tokens of the input program and assembles the tokens together to a parse tree.
    A parser typically:
    * Uses a context-free grammar (CFG) to match the token stream.
    * Performs a derivation by matching the token stream against the grammar rules. 
    * Creates a parse tree. 

* **Abstract Syntax Tree (AST)**: The purpose of the AST is to provide a standardized version of the program suitable for later analysis.
    The AST is usually build by associating tree construction code with the grammar’s production rules.
    As the AST is being built, the tool builds a **symbol table** alongside it. 
    For each identifier in the program, the symbol associates the identifier with its type and a reference to its declaration or definition.

* **Semantic Analysis**: With the AST and the symbol table, the tool is now equipped to perform type checking. An advanced static analysis tool 
    has to do just as much work related to type checking as a compiler does.
    A static analysis tool might perform additional transformations on the AST or might generate its own variety of intermediate representation 
    suitable to its needs:
    * Most tools build a **control flow graph** on top of the AST.
    * A **call graph** represents potential control flow between functions or methods.

## References

* Brian Chess, Jacob West. **Secure Programming with Static Analysis**. Addison-Wesley, 2007

* Terence Parr. **Language Implementation Patterns**. The Pragmatic Bookshelf, 2010 

* [Python Static Analysis Tools](https://luminousmen.com/post/python-static-analysis-tools)

* [Youtube: Static Code Analysis with Python](https://youtu.be/mfXIJ-Fu5Fw)

*Egon Teiniker, 2020-2022, GPL v3.0*