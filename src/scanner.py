import sys
import ply.lex as lex
from ply.lex import TOKEN

'''D     = r'([0-9])'
L     = r'([a-zA-Z_])'
H     = r'([a-fA-F0-9])'
E     = r'([Ee][+-]?{D}+)'
FS    = r'(f|F|l|L)'
IS    = r'((u|U|l|L)*)'
'''


reserved ={ 
	'auto' : 'AUTO',
	'break' : 'BREAK',
	'case' : 'CASE',
	'char' : 'CHAR',
	'const' : 'CONST',
	'continue' : 'CONTINUE',
	'default' : 'DEFAULT',
	'do' : 'DO',
	'double' : 'DOUBLE',
	'else' : 'ELSE',
	'enum' : 'ENUM',
	'extern' : 'EXTERN',
	'float' : 'FLOAT',
	'for' : 'FOR',
	'goto' : 'GOTO',
	'if' : 'IF',
	'int' : 'INT',
	'long' : 'LONG',
	'register' : 'REGISTER',
	'return' : 'RETURN',
	'short' : 'SHORT',
	'signed' : 'SIGNED',
	'sizeof' : 'SIZEOF',
	'static' : 'STATIC',
	'struct' : 'STRUCT',
	'switch' : 'SWITCH',
	'typedef' : 'TYPEDEF',
	'union' : 'UNION',
	'unsigned' : 'UNSIGNED',
	'void' : 'VOID',
	'volatile' : 'VOLATILE',
	'while' : 'WHILE',
}


tokens = [
#	'D',
#	'L',
#	'H',
#	'E',
#	'FS',
#	'IS',
#	'NUMBER',
#	'comment()',
#	'comment1()',
#    'CHECK_TYPE',
    'COMMENT',
    'COMMENT1',
    'COMMENT2',
	'CONSTANT',
	'CONSTANT1',
	'CONSTANT2',
	'CONSTANT3',
	'CONSTANT4',
	'CONSTANT5',
	'CONSTANT6',
	'CONSTANT7',
	'IDENTIFIER',
	'STRING_LITERAL',
	'ELLIPSIS',
	'RIGHT_ASSIGN',
	'LEFT_ASSIGN',
	'ADD_ASSIGN',
	'SUB_ASSIGN',
	'MUL_ASSIGN',
	'DIV_ASSIGN',
	'MOD_ASSIGN',
	'AND_ASSIGN',
	'XOR_ASSIGN',
	'OR_ASSIGN',
	'RIGHT_OP',
	'LEFT_OP',
	'INC_OP',
	'DEC_OP',
	'PTR_OP',
	'AND_OP',
	'OR_OP',
	'LE_OP',
	'GE_OP',
	'EQ_OP',
	'NE_OP',
	'TYPE_NAME',
] 
tokens = list(reserved.values()) + tokens

literals = (
	';',
	'{',
	'}',
	',',
	':',
	'=',
	'(',
	')',
	'[',
	']',
	'.',
	'&',
	'!',
	'~',
	'-',
	'+',
	'*',
	'/',
	'%',
	'<',
	'>',
	'^',
	'|',
	'?',
)




#token definition
D     = r'([0-9])'
L     = r'([a-zA-Z_])'
H     = r'([a-fA-F0-9])'
E     = r'([Ee][+-]?' + D + r'+)'  #r'([Ee][+-]?{D}+)'
FS    = r'(f|F|l|L)'
IS    = r'((u|U|l|L)*)'
#t_check_type()
#{L}({L}|{D})*

t_ignore_COMMENT = r'//.*'
t_ignore_COMMENT2 = r'\#.*'

#r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'

#IDENTIFIER = r'(' + L + r'(' + L + r'|' + D + r')*)'

#CONSTANT1 = r'(0[xX]' + H + r'+' + IS + r'?)'   #r'0[xX]{H}+{IS}?' -->  r'0[xX][a-fA-F0-9]+(u|U|l|L)*'
#CONSTANT2 = r'(0' + D + r'+' + IS + r'?)'  #r'0{D}+{IS}?'  ---> r'0[0-9]+(u|U|l|L)*?'
#CONSTANT3 = r'(' + D + r'+' + IS + r'?)'  #r'{D}+{IS}?'  ----> r'[0-9]+(u|U|l|L)*?'
CONSTANT4 = r'(' + L + r'?\'(\\.|[^\\\'])+\')'  #r"L?'(\\.|[^\\'])+'"  ---> 

#CONSTANT5 = r'(' + D + r'+' + E + FS + r'?)'  #r'{D}+{E}{FS}?'  ---> r'[0-9]+[Ee][+-]?[0-9]+(f|F|l|L)*?'
#CONSTANT6 = r'(' + D + r'*\.' + D + r'+' + r'(' + E + r')?' + FS + r'?)'  #r'{D}*"."{D}+({E})?{FS}?' --> r'[0-9]*\.[0-9]+([Ee][+-]?[0-9]+)?(f|F|l|L)?'
#CONSTANT7 = r'(' + D + r'+\.' + D + r'*(' + E + r')?' + FS + r'?)'  #r'{D}+"."{D}*({E})?{FS}?' -->  r'[0-9]+\.[0-9]*([Ee][+-]?[0-9]+)?(f|F|l|L)?'

t_STRING_LITERAL = r'[a-zA-Z_]?\"(\\.|[^\\"])*\"'

#t_ELLIPSIS = r'...'
t_RIGHT_ASSIGN = r'>>='
t_LEFT_ASSIGN = r'<<='
t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN = r'-='
t_MUL_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_AND_ASSIGN = r'&='
t_XOR_ASSIGN = r'^='
t_OR_ASSIGN = r'\|='
t_RIGHT_OP = r'>>'
t_LEFT_OP = r'<<'
t_INC_OP = r'\+\+'
t_DEC_OP = r'--'
t_PTR_OP = r'->'
t_AND_OP = r'&&'
t_OR_OP = r'\|\|'
t_LE_OP = r'<='
t_GE_OP = r'>='
t_EQ_OP = r'=='
t_NE_OP = r'!='

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\v\n\f'

def t_COMMENT1(t):
    r'/\*.*(\n.*)*\*/'
    pass

'''@TOKEN(IDENTIFIER)
def t_CHECK_TYPE(t):
#    r'(' + L + r'(' + L + r'|' + D + r')*)'
#    r''
  #  tok = t.lexer.token()
#    print t.value, t.type
#    print reserved.keys()
    if t.value in reserved.keys():
      #  return reserved[t.value]
        t.type = reserved[t.value]
    else:
        t.type = 'IDENTIFIER'
 #   print t.value, t.type
    return t
'''

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')
    return t

#@TOKEN(CONSTANT1)
def t_CONSTANT1(t):
    r'0[xX][a-fA-F0-9]+(u|U|l|L)*'
    t.type = 'CONSTANT'
    return t

#@TOKEN(CONSTANT2)
def t_CONSTANT2(t):
    r'0[0-9]+(u|U|l|L)*?'
    t.type = 'CONSTANT'
    return t
#@TOKEN(CONSTANT3)
def t_CONSTANT3(t):
    r'[0-9]+(u|U|l|L)*?'
    t.type = 'CONSTANT'
    return t
@TOKEN(CONSTANT4)
def t_CONSTANT(t):
    t.type = 'CONSTANT'
    return t
#@TOKEN(CONSTANT5)
def t_CONSTANT5(t):
    r'[0-9]+[Ee][+-]?[0-9]+(f|F|l|L)*?'
    t.type = 'CONSTANT'
    return t
#@TOKEN(CONSTANT6)
def t_CONSTANT6(t):
    r'[0-9]*\.[0-9]+([Ee][+-]?[0-9]+)?(f|F|l|L)?'
    t.type = 'CONSTANT'
    return t
#@TOKEN(CONSTANT7)
def t_CONSTANT7(t):
    r'[0-9]+\.[0-9]*([Ee][+-]?[0-9]+)?(f|F|l|L)?'
    t.type = 'CONSTANT'
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

fd = open(sys.argv[1], 'r')
data = fd.read()
fd.close()

# Give the lexer some input
lexer.input(data)

#print tokens

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value)

