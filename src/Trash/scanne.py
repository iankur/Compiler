D     =      r'[0-9]'
L     =      r'[a-zA-Z_]'
H     =      r'[a-fA-F0-9]'
E     =      r'[Ee][+-]?{D}+'
FS    =      r'(f|F|l|L)'
IS    =      r'(u|U|l|L)*'



reserved = (
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
)


tokens = (
#	'NUMBER',
	'comment()',
	'comment1()',
	'check_type()',
	'CONSTANT',
	'CONSTANT',
	'CONSTANT',
	'CONSTANT',
	'CONSTANT',
	'CONSTANT',
	'CONSTANT',
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
) + list(reserved.values())



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

t_check_type() = r'{L}({L}|{D})*'

t_CONSTANT = r'0[xX]{H}+{IS}?'
t_CONSTANT = r'0{D}+{IS}?'
t_CONSTANT = r'{D}+{IS}?'
t_CONSTANT = r'L?'(\\.|[^\\'])+''

t_CONSTANT = r'{D}+{E}{FS}?'
t_CONSTANT = r'{D}*"."{D}+({E})?{FS}?'
t_CONSTANT = r'{D}+"."{D}*({E})?{FS}?'

t_STRING_LITERAL = r'L?\"(\\.|[^\\"])*\"'

t_ELLIPSIS = r'...'
t_RIGHT_ASSIGN = r'>>='
t_LEFT_ASSIGN = r'<<='
t_ADD_ASSIGN = r'+='
t_SUB_ASSIGN = r'-='
t_MUL_ASSIGN = r'*='
t_DIV_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_AND_ASSIGN = r'&='
t_XOR_ASSIGN = r'^='
t_OR_ASSIGN = r'|='
t_RIGHT_OP = r'>>'
t_LEFT_OP = r'<<'
t_INC_OP = r'++'
t_DEC_OP = r'--'
t_PTR_OP = r'->'
t_AND_OP = r'&&'
t_OR_OP = r'||'
t_LE_OP = r'<='
t_GE_OP = r'>='
t_EQ_OP = r'=='
t_NE_OP = r'!='

