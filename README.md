# YAPL (Your Own Programming Language)-Interpreter
A parser and compiler for a self-created programming language, built from scratch on Python. 

Three different components go into designing your own language and an associated interpreter for it: lexer, parser and interpreter. The lexer basically takes a sequence of characters (ex. Your high level code) as input and outputs a sequence of tokens. Next up is the parser. The parser takes these tokens and outputs a parse tree where each branch is filled with your expressions or statements. Finally, you have the interpreter which goes through each branch, evaluates it, and executes your statements.
