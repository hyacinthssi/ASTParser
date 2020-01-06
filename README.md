#CSC153

#AST Parser
----------------------------------------------------------------------------------------------------

Features: 

LEXER a.k.a Lexical Analyzer or Tokenizer
    - is a program that breaks down the input source code into a sequence of lexemes.
      It reads the input source code character by character, recognizes the lexemes and outputs
      a sequence of tokens describing the lexemes.

PARSER (Recursive-Descent Parsing Technique)
    - takes input in the form of a sequence of tokens or program instructions and usually builds
      a data structure in the form of a parse tree or an abstract syntax tree.

ABSTRACT SYNTAX TREE (AST)
    - a tree representation of the abstract syntactic structure of source code written in a 
      programming language.
      
----------------------------------------------------------------------------------------------------    

#Run "ParserMain" :

        python ParserMain.py

----------------------------------------------------------------------------------------------------

#Character.py
    - wraps a single character that the scanner retrieves from the text file. 

#Scanner.py
    - reads the text file one character at a time. For each character, it keeps track of the 
      line and character position where the character was found. Each time the scanner is called,
      it reads the next character from the file and returns it.

#Lexer.py
    - divides the input text into smaller parts called tokens.

#Symbols.py
    - specifies the symbol.

#Token.py
    - wraps its cargo -- a string of characters that is the text of the token. 
      In addition, the token will hold information about the location
      of the token (the location of its first character) in the textFile.

#LexerMain.py
    - set up a string of textFile, creates a lexer object to tokenize that textFile,
      and then displays the tokens that it gets back from the lexer.

#Parser.py
    - produce AST.
    - obtains a string of tokens from lexer and verifies that the string can be the grammar for
      the source language

#AstNode.py
    - used during parsing. The goal of the parser is to construct an AST.

#ParserMain.py
    - set up a string of textFile, the displays the ast of the parsed textFile.
    
