
all: ../bin/parser

lex.yy.c: scan.l y.tab.h
	lex scan.l

y.tab.h y.tab.c: grammar.y
	bison -dy grammar.y

../bin/lexer: lex.yy.c y.tab.c y.tab.h
	gcc -g lex.yy.c -o ../bin/lexer

../bin/parser: grammar.y y.tab.c y.tab.h
	gcc -g y.tab.c -o ../bin/scanner -lfl
