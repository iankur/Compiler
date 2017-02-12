# README #

This project is for the course CS335 at IITK. It involves designing of a compiler.

### Project Specifications ###

* Source Language : C
* Implementation Language : Python
* Target Language : MIPS

### Team Members ###

* Ankur Kumar
* Kartik Raj
* Shubham Kumar Pandey

### Work Flow ###

* Downloaded yacc grammar and lex input specifications for C language
* Implemented stand alone scanner/lexer
* Implemented parser integrated with scanner
* Added action rules to output the correct parse tree

### Testing ###

* For using stand alone scanner on a file in test directory, run : python scanner.py ../test/<file>
* Parse a file in test directory using : python parser.py ../test/<file>

Note: There is no need to build anything in python, so bin directory is empty