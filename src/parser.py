import sys
import pydot
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from scanner import tokens

#start = 'translation_unit'

class Node:
    count = 0 
   # type = 'Node (unspecified)'
    shape = 'ellipse'

    def __init__(self, type, children=None):
        self.ID = str(Node.count)
        self.type = type
        Node.count += 1
        if not children: self.children = []
        elif hasattr(children, '__len__'):
            self.children = children
        else:
            self.children = [children]
        self.next = []

    def makegraphicaltree(self, dot=None, edgeLabels=True):
        if not dot: dot = pydot.Dot()

#        print self.type
        if self.type == ',' : dot.add_node(pydot.Node(self.ID, label='","', shape=self.shape))
        else : dot.add_node(pydot.Node(self.ID, label=self.type, shape=self.shape))
        label = edgeLabels and len(self.children)-1
        for i,c in enumerate(self.children):
            if not isinstance(c, Node) :
#                print "%s" %(c)
                c = Node(c, None)
  #              print c.type
            c.makegraphicaltree(dot, edgeLabels)
            edge = pydot.Edge(self.ID, c.ID)
            if label:
                edge.set_label(str(i))
            dot.add_edge(edge)
        return dot 

class ProgramNode(Node):
    type = 'Program'

class TokenNode(Node):
    type = 'token'

    def __init__(self, tok):
        Node.__init__(self)
        self.tok = tok 

    def __repr__(self):
        return repr(self.tok)

def p_translation_unit(p):
    '''translation_unit : external_declaration
                        | translation_unit external_declaration'''
    print 'translation_unit'
    if len(p) == 2 : p[0] = Node('translational_unit', p[1])
    else : p[0] = Node('translational_unit', [p[1], p[2]])
#    pass

def p_primary_expression(p):
    '''primary_expression : IDENTIFIER 
                            | CONSTANT 
                            | STRING_LITERAL 
                            | '(' expression ')' '''
    if (len(p) == 2):
        p[0] = Node('primary_expression', [p[1]])
    else:
        p[0] = Node('primary_expression', p[2]) 
    print 'primary_expression', p[1]
 #   pass

def p_postfix_expression(p):
    '''postfix_expression : primary_expression
                            | postfix_expression '[' expression ']'
                            | postfix_expression '(' ')'
                            | postfix_expression '(' argument_expression_list ')'
                            | postfix_expression '.' IDENTIFIER
                            | postfix_expression PTR_OP IDENTIFIER
                            | postfix_expression INC_OP
                            | postfix_expression DEC_OP'''
    print 'postfix_expression', p[1]
    if len(p) == 2 : p[0] = Node('postfix_expression', p[1])
    elif len(p) == 3 : p[0] = Node('postfix_expression', [p[1], p[2]])
    elif len(p) == 4 : p[0] = Node('postfix_expression', [p[1], p[2], p[3]])
    else : p[0] = Node('postfix_expression', [p[1], p[2], p[3], p[4]])
  #  pass

def p_argument_expression_list(p):
    '''argument_expression_list : assignment_expression
                                | argument_expression_list ',' assignment_expression'''
    print 'argument_expression_list'
    if len(p) == 2 : p[0] = Node('argument_expression_list', p[1])
    else : p[0] = Node('argument_expression', [p[1], p[2], p[3]])
#    pass

def p_unary_expression(p):
    '''unary_expression : postfix_expression
                        | INC_OP unary_expression
                        | DEC_OP unary_expression
                        | unary_operator cast_expression
                        | SIZEOF unary_expression
                        | SIZEOF '(' type_name ')' '''
    print 'unary_expression'
    if len(p) == 2 : p[0] = Node('unary_expression', p[1])
    elif len(p) == 3 : p[0] = Node('unary expression', [p[1], p[2]])
    else : p[0] = Node('unary_expression', [p[1], p[2], p[3], p[4]])
#    pass

def p_unary_operator(p):
    '''unary_operator : '&'
                        | '*'
                        | '+'
                        | '-'
                        | '~'
                        | '!' '''
#    p[0] = p[1]
    print 'unary_operator', p[1]
    p[0] = Node('unary_operator', [p[1]])
#    pass

def p_cast_expression(p):
    '''cast_expression : unary_expression
                        | '(' type_name ')' cast_expression'''
    print 'cast expression'
    if len(p) == 2 : p[0] = Node('cast_expression', p[1])
    else : p[0] = Node('cast_expression', [p[1], p[2], p[3], p[4]])
#    pass

def p_multiplicative_expression(p):
    '''multiplicative_expression : cast_expression
                                | multiplicative_expression '*' cast_expression
                                | multiplicative_expression '/' cast_expression
                                | multiplicative_expression '%' cast_expression'''
    print 'multicative expression'
    if len(p) == 2 : p[0] = Node('multiplicative_expression', p[1])
    else : p[0] = Node('multiplicative expression', [p[1], p[2], p[3]])
#    pass

def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                            | additive_expression '+' multiplicative_expression
                            | additive_expression '-' multiplicative_expression'''
    print 'additive expression'
    if len(p) == 2 : p[0] = Node('additive_expression', p[1])
    else : p[0] = Node('additive_expression', [p[1], p[2], p[3]])
#    print p[1]
#    pass

def p_shift_expression(p):
    '''shift_expression : additive_expression
                        | shift_expression LEFT_OP additive_expression
                        | shift_expression RIGHT_OP additive_expression'''
    print 'shift expression'
    if len(p) == 2 : p[0] = Node('shift_expression', p[1])
    else : p[0] = Node('shift_expression', [p[1], p[2], p[3]])
#    pass

def p_relational_expression(p):
    '''relational_expression : shift_expression
                                | relational_expression '<' shift_expression
                                | relational_expression '>' shift_expression
                                | relational_expression LE_OP shift_expression
                                | relational_expression GE_OP shift_expression'''
    print 'relational expression'
    if len(p) == 2 : p[0] = Node('relational_expression', p[1])
    else : p[0] = Node('relational_expression', [p[1], p[2], p[3]])
#    pass

def p_equality_expression(p):
    '''equality_expression : relational_expression
                            | equality_expression EQ_OP relational_expression
                            | equality_expression NE_OP relational_expression'''
    print 'equality expression'
    if len(p) == 2 : p[0] = Node('equality_expression', p[1])
    else : p[0] = Node('equality_expression', [p[1], p[2], p[3]])
#    pass

def p_and_expression(p):
    '''and_expression : equality_expression
                        | and_expression '&' equality_expression'''
    print 'and expression'
    if len(p) == 2 : p[0] = Node('and_expression', p[1])
    else : p[0] = Node('and_expression', [p[1], p[2], p[3]])
#    pass

def p_exclusive_or_expression(p):
    '''exclusive_or_expression : and_expression
                                | exclusive_or_expression '^' and_expression'''
    print 'exclusive or expression'
    if len(p) == 2 : p[0] = Node('exclusive_expression', p[1])
    else : p[0] = Node('exclusive', [p[1], p[2], p[3]])
#    pass

def p_inclusive_or_expression(p):
    '''inclusive_or_expression : exclusive_or_expression
                                | inclusive_or_expression '|' exclusive_or_expression'''
    print 'inclusive or expression'
    if len(p) == 2 : p[0] = Node('inclusive_or_expression', p[1])
    else : p[0] = Node('inclusive_or_expression', [p[1], p[2], p[3]])
#    pass

def p_logical_and_expression(p):
    '''logical_and_expression : inclusive_or_expression
                                | logical_and_expression AND_OP inclusive_or_expression'''
    print 'logical and expression'
    if len(p) == 2 : p[0] = Node('logical_and_expression', p[1])
    else : p[0] = Node('logical_and_expression', [p[1], p[2], p[3]])
#    pass

def p_logical_or_expression(p):
    '''logical_or_expression : logical_and_expression
                                | logical_or_expression OR_OP logical_and_expression'''
    print 'logical or expression'
    if len(p) == 2 : p[0] = Node('logical_or_expression', p[1])
    else : p[0] = Node('logical_or_expression', [p[1], p[2], p[3]])
#    pass

def p_conditional_expression(p):
    '''conditional_expression : logical_or_expression
                                | logical_or_expression '?' expression ':' conditional_expression'''
    print 'conditional expression'
    if len(p) == 2 : p[0] = Node('conditional_expression', p[1])
    else : p[0] = Node('conditional_expression', [p[1], p[2], p[3], p[4], p[5]])
#    pass

def p_assignment_expression(p):
    '''assignment_expression : conditional_expression
                                | unary_expression assignment_operator assignment_expression'''
    print 'assignment expression'
    if len(p) == 2 : p[0] = Node('assignment_expression', p[1])
    else : p[0] = Node('assignment_expression', [p[1], p[2], p[3]])
#    pass

def p_assignment_operator(p):
    '''assignment_operator : '='
                            | MUL_ASSIGN
                            | DIV_ASSIGN
                            | MOD_ASSIGN
                            | ADD_ASSIGN
                            | SUB_ASSIGN
                            | LEFT_ASSIGN
                            | RIGHT_ASSIGN
                            | AND_ASSIGN
                            | XOR_ASSIGN
                            | OR_ASSIGN'''
#    p[0] = p[1]
    print 'assignment operator', p[1]
    p[0] = Node('assignment_operator', [p[1]])
#    pass

def p_expression(p):
    '''expression : assignment_expression
                    | expression ',' assignment_expression'''
    print 'expression'
    if len(p) == 2 : p[0] = Node('expression', p[1])
    else : p[0] = Node('expression', [p[1], p[2], p[3]])
#    pass

def p_constant_expression(p):
    '''constant_expression : conditional_expression'''
    print 'constant expression'
    p[0] = Node('constant_expression', p[1])
#    pass

def p_declaration(p):
    '''declaration : declaration_specifiers ';'
                    | declaration_specifiers init_declarator_list ';' '''
    print 'declaration'
    if len(p) == 3 : p[0] = Node('declaration', [p[1], p[2]])
    else : p[0] = Node('declaration', [p[1], p[2], p[3]])
#    pass

def p_declaration_specifiers(p):
    '''declaration_specifiers : storage_class_specifier
                                | storage_class_specifier declaration_specifiers
                                | type_specifier
                                | type_specifier declaration_specifiers
                                | type_qualifier
                                | type_qualifier declaration_specifiers'''
    print 'declaration specifiers'
    if (len(p) == 2): p[0] = Node('declaration_specifiers', p[1])
    else : p[0] = Node('declaration_specifiers', [p[1], p[2]])
#    pass

def p_init_declarator_list(p):
    '''init_declarator_list : init_declarator
                            | init_declarator_list ',' init_declarator'''
    print 'init declarator list'
    if len(p) == 2 : p[0] = Node('init_declarator_list', p[1])
    else : p[0] = Node('init_declarator_list', [p[1], p[2], p[3]])
#    pass

def p_init_declarator(p):
    '''init_declarator : declarator
                        | declarator '=' initializer'''
    print 'init declarator'
    if len(p) == 2:
        p[0] = Node('init_declarator', p[1])
    else:
        p[0] = Node('init_declarator', [p[2], p[1], p[3]])
#    pass

def p_storage_class_specifier(p):
    '''storage_class_specifier : TYPEDEF
                                | EXTERN
                                | STATIC
                                | AUTO
                                | REGISTER'''
    print 'storage class specifier'
    p[0] = Node('storage_class_classifier', [p[1]])
#    print p[0]
#    pass

def p_type_specifier(p):
    '''type_specifier : VOID
                        | CHAR
                        | SHORT
                        | INT
                        | LONG
                        | FLOAT
                        | DOUBLE
                        | SIGNED
                        | UNSIGNED
                        | struct_or_union_specifier
                        | enum_specifier
                        | TYPE_NAME'''
    print 'type specifier'#, p[0], p[1]
    p[0] = Node('type_specifier', [p[1]])
#    pass

def p_struct_or_union_specifier(p):
    '''struct_or_union_specifier : struct_or_union IDENTIFIER '{' struct_declaration_list '}'
                                    | struct_or_union '{' struct_declaration_list '}'
                                    | struct_or_union IDENTIFIER'''
    print 'struct or union specifier'
    if len(p) == 3 : p[0] = Node('struct_or_union_specifier', [p[1], p[2]])
    elif len(p) == 4 : p[0] = Node('struct_or_union_specifier', [p[1], p[2], p[3]])
    else : p[0] = Node('struct_or_union_specifier', [p[1], p[2], p[3], p[4]])
#    pass

def p_struct_or_union(p):
    '''struct_or_union : STRUCT
                        | UNION'''
    print 'struct or union'
    p[0] = Node('struct_or_union', [p[1]])
#    pass

def p_struct_declaration_list(p):
    '''struct_declaration_list : struct_declaration
                                | struct_declaration_list struct_declaration'''
    print 'struct declaration list'
    if len(p) == 2 : p[0] = Node('struct_declaration_list', p[1])
    else : p[0] = Node('struct_declaration_list', [p[1], p[2]])
#    pass

def p_struct_declaration(p):
    '''struct_declaration : specifier_qualifier_list struct_declarator_list ';' '''
    print 'struct declaration'
    p[0] = Node('struct_declaration', [p[1], p[2]])
#    pass

def p_specifier_qualifier_list(p):
    '''specifier_qualifier_list : type_specifier specifier_qualifier_list
                                | type_specifier
                                | type_qualifier specifier_qualifier_list
                                | type_qualifier'''
    print 'specifier qualifier list'
    if len(p) == 2 : p[0] = Node('specifier_qualifier_list', p[1])
    else : p[0] = Node('specifier_qualifier_list', [p[1], p[2]])
#    pass

def p_struct_declarator_list(p):
    '''struct_declarator_list : struct_declarator
                                | struct_declarator_list ',' struct_declarator'''
    print 'struct declarator list'
    if len(p) == 2 : p[0] = Node('struct_declarator_list', p[1])
    else : p[0] = Node('struct_declarator_list', [p[1], p[2], p[3]])
#    pass

def p_struct_declarator(p):
    '''struct_declarator : declarator
                            | ':' constant_expression
                            | declarator ':' constant_expression'''
    print 'struct declarator'
    if len(p) == 2 : p[0] = Node('struct_declarator', p[1])
    elif len(p) == 3 : p[0] = Node('struct_declarator', [p[1], p[2], p[3]])
#    pass

def p_enum_specifier(p):
    '''enum_specifier : ENUM '{' enumerator_list '}'
                        | ENUM IDENTIFIER '{' enumerator_list '}'
                        | ENUM IDENTIFIER'''
    print 'enum specifier'
    if len(p) == 3 : p[0] = Node('enum_specifier', [p[1], p[2]])
    elif len(p) == 5 : p[0] = Node('enum_specifier', [p[1], p[2], p[3], p[4]])
    else : p[0] = Node('enum_specifier', [p[1], p[2], p[3], p[4], p[5]])
#    pass

def p_enumerator_list(p):
    '''enumerator_list : enumerator
                        | enumerator_list ',' enumerator'''
    print 'enumerator list'
    if len(p) == 2 : p[0] = Node('enumerator_list', p[1])
    else : p[0] = Node('enumerator_list', [p[1], p[2], p[3]])
#    pass

def p_enumerator(p):
    '''enumerator : IDENTIFIER
                    | IDENTIFIER '=' constant_expression'''
    print 'enumerator'
    if len(p) == 2 : p[0] = Node('enumerator', [p[1]])
    else : p[0] = Node('enumerator', [p[1], p[2], p[3]])
#    pass

def p_type_qualifier(p):
    '''type_qualifier : CONST
                        | VOLATILE'''
    print 'type qualifier'
    p[0] = Node('type_qualifier', [p[1]])
#    pass

def p_declarator(p):
    '''declarator : pointer direct_declarator
                    | direct_declarator'''
    print 'declarator'#, p[0], p[1]
    if len(p) == 2 : p[0] = Node('declarator', p[1])
    else : p[0] = Node('declarator', [p[1], p[2]])
#    pass

def p_direct_declarator(p):
    '''direct_declarator : IDENTIFIER
                            | '(' declarator ')'
                            | direct_declarator '[' constant_expression ']'
                            | direct_declarator '[' ']'
                            | direct_declarator '(' parameter_type_list ')'
                            | direct_declarator '(' identifier_list ')'
                            | direct_declarator '(' ')' '''
    print 'direct declarator'
    if len(p) == 2 : p[0] = Node('direct_declarator', [p[1]])
    elif len(p) == 4 : p[0] = Node('direct_declarator', [p[1], p[2], p[3]])
    else : p[0] = Node('direct_declarator', [p[1], p[2], p[3], p[4]])
#    if len(p) == 2 : p[0] = p[1]
#    pass

def p_pointer(p):
    '''pointer : '*'
                | '*' type_qualifier_list
                | '*' pointer
                | '*' type_qualifier_list pointer'''
    print 'pointer'
    if len(p) ==2 : p[0] = Node('pointer', [p[1]])
    else : p[0] = Node('pointer', [p[1], p[2]])
#    pass

def p_type_qualifier_list(p):
    '''type_qualifier_list : type_qualifier
                            | type_qualifier_list type_qualifier'''
    print 'type qualifier list'
    if len(p) == 2 : p[0] = Node('type_qualifier_list', p[1])
    else : p[0] = Node('type_qualifier_list', [p[1], p[2]])
#    pass

def p_parameter_type_list(p):
    '''parameter_type_list : parameter_list
                            | parameter_list ',' ELLIPSIS'''
    print 'parameter type list'
    if len(p) == 2 : p[0] = Node('parameter_type_list', p[1])
    else : p[0] = Node('parameter_type_list', [p[1], p[2], p[3]])
#    pass

def p_parameter_list(p):
    '''parameter_list : parameter_declaration
                        | parameter_list ',' parameter_declaration'''
    print 'parameter list'
    if len(p) == 2 : p[0] = Node('parameter', p[1])
    else : p[0] = Node('parameter', [p[1], p[2], p[3]])
#    pass

def p_parameter_declaration(p):
    '''parameter_declaration : declaration_specifiers declarator
                                | declaration_specifiers abstract_declarator
                                | declaration_specifiers'''
    print 'parameter declaration'
    if len(p) == 2 : p[0] = Node('parameter_declaration', p[1])
    else : p[0] = Node('parameter_declaration', [p[1], p[2]])
#    pass

def p_identifier_list(p):
    '''identifier_list : IDENTIFIER
                        | identifier_list ',' IDENTIFIER'''
    print 'identifier list'
    if len(p) == 2 : p[0] = Node('identifier_list', [p[1]])
    else : p[0] = Node('identifier_list', [p[1], p[2], p[3]])
#    pass

def p_type_name(p):
    '''type_name : specifier_qualifier_list
                    | specifier_qualifier_list abstract_declarator'''
    print 'tyoe name'
    if len(p) == 2 : p[0] = Node('type_name', p[1])
    else : p[0] = Node('type_name', [p[1], p[2]])
#    pass

def p_abstract_declarator(p):
    '''abstract_declarator : pointer
                            | direct_abstract_declarator
                            | pointer direct_abstract_declarator'''
    print 'abstract declarator'
    if len(p) == 2 : p[0] = Node('abstract_declarator', p[1])
    else : p[0] = Node('abstract_declarator', [p[1], p[2]])
#    pass

def p_direct_abstract_declarator(p):
    '''direct_abstract_declarator : '(' abstract_declarator ')'
                                    | '[' ']'
                                    | '[' constant_expression ']'
                                    | direct_abstract_declarator '[' ']'
                                    | direct_abstract_declarator '[' constant_expression ']'
                                    | '(' ')'
                                    | '(' parameter_type_list ')'
                                    | direct_abstract_declarator '(' ')'
                                    | direct_abstract_declarator '(' parameter_type_list ')' '''
    print 'direct abstract declarator'
    if len(p) == 3 : p[0] = Node('direct_abstract_declarator', [p[1], p[2]])
    elif len(p) == 4 : p[0] = Node('direct_abstract_declarator', [p[1], p[2], p[3]])
    elif len(p) == 5 : p[0] = Node('direct_abstract_declarator', [p[1], p[2], p[3], p[4]])
#    pass

def p_initializer(p):
    '''initializer : assignment_expression
                    | '{' initializer_list '}'
                    | '{' initializer_list ',' '}' '''
    print 'initializer'
    if len(p) == 2 : p[0] = Node('initializer', p[1])
    elif len(p) == 4 : p[0] = Node('initializer', [p[1], p[2], p[3]])
    else : p[0] = Node('initializer', [p[1], p[2], p[3], p[4]])
#    pass

def p_initializer_list(p):
    '''initializer_list : initializer
                        | initializer_list ',' initializer'''
    print 'initializer list'
    if len(p) == 2 : p[0] = Node('initializer_list', p[1])
    else : p[0] = Node('initializer_list', [p[1], p[2], p[3]])
#    pass

def p_statement(p):
    '''statement : labeled_statement
                    | compound_statement
                    | expression_statement
                    | selection_statement
                    | iteration_statement
                    | jump_statement'''
    print 'statement'
    p[0] = Node('statement', p[1])
#    pass

def p_labeled_statement(p):
    '''labeled_statement : IDENTIFIER ':' statement
                            | CASE constant_expression ':' statement
                            | DEFAULT ':' statement'''
    print 'labeled statement'
    if len(p) == 4 : p[0] = Node('labeled_statement', [p[1], p[2], p[3]])
    else : p[0] = Node('labeled_statement', [p[1], p[2], p[3], p[4]])
#    pass

def p_compound_statement(p):
    '''compound_statement : '{' '}'
                            | '{' statement_list '}'
                            | '{' declaration_list '}'
                            | '{' declaration_list statement_list '}' '''
    print 'compound statement'
    if len(p) == 3 : p[0] = Node('compound_statement', [p[1], p[2]])
    elif len(p) == 4 : p[0] = Node('compound_statement', [p[1], p[2], p[3]])
    else : p[0] = Node('compound_statement', [p[1], p[2], p[3], p[4]])   
#    pass

def p_declaration_list(p):
    '''declaration_list : declaration
                        | declaration_list declaration'''
    print 'declaration list'
    if len(p) == 2 : p[0] = Node('declaration_list', p[1])
    else : p[0] = Node('declaration_list', [p[1], p[2]])
#    pass

def p_statement_list(p):
    '''statement_list : statement
                        | statement_list statement'''
    print 'statement list', p[1]
    if len(p) == 2 : p[0] = Node('statement_list', p[1])
    else : p[0] = p[0] = Node('statement_list', [p[1], p[2]])
#    pass

def p_expression_statement(p):
    '''expression_statement : ';'
                            | expression ';' '''
    print 'expression statement'
    if len(p) == 2 : p[0] = Node('expresson_statement', p[1])
    else : p[0] = Node('expression_statement', [p[1], p[2]])
#    pass

def p_selection_statement(p):
    '''selection_statement : IF '(' expression ')' statement
                            | IF '(' expression ')' statement ELSE statement
                            | SWITCH '(' expression ')' statement'''
    print 'selection statement'
    if len(p) == 6 : p[0] = Node('selection_statement', [p[1], p[2], p[3], p[4], p[5]])
    else : p[0] = Node('selection_statement', [p[1], p[2], p[3], p[4], p[5], p[6], p[7]])
#    pass

def p_iteration_statement(p):
    '''iteration_statement : WHILE '(' expression ')' statement
                            | DO statement WHILE '(' expression ')' ';'
                            | FOR '(' expression_statement expression_statement ')' statement
                            | FOR '(' expression_statement expression_statement expression ')' statement'''
    print 'iteration statement', p[1], p[2], p[3]
    if len(p) == 6 : p[0] = Node('iteration_statement', [p[1], p[2], p[3], p[4], p[5]])
    elif len(p) == 7 : p[0] = Node('iteration_statement', [p[1], p[2], p[3], p[4], p[5], p[6]])
    else : p[0] = Node('iteration_statement', [p[1], p[2], p[3], p[4], p[5], p[6], p[7]])
#    pass

def p_jump_statement(p):
    '''jump_statement : GOTO IDENTIFIER ';'
                        | CONTINUE ';'
                        | BREAK ';'
                        | RETURN ';'
                        | RETURN expression ';' '''
    print 'jump statement'
    if len(p) == 3 : p[0] = Node('jump_statement', [p[1], p[2]])
    elif len(p) == 4 : p[0] = Node('jump_statement', [p[1], p[2], p[3]])
#    pass

#def p_translation_unit(p):
  #  '''translation_unit : external_declaration
   #                     | translation_unit external_declaration'''
#    pass
 #   print "translation unit\n"

def p_external_declaration(p):
    '''external_declaration : function_definition
                            | declaration'''
    print 'external declaration'
    p[0] = Node('external_declaration', p[1])
#    print "external declaration\n"  
#    pass

def p_function_definition(p):
    '''function_definition : declaration_specifiers declarator declaration_list compound_statement
                            | declaration_specifiers declarator compound_statement
                            | declarator declaration_list compound_statement
                            | declarator compound_statement'''
    print 'function definition'
    if len(p) == 3 : p[0] = Node('function_definition', [p[1], p[2]])
    elif len(p) == 4 : p[0] = Node('function_definition', [p[1], p[2], p[3]])
    else : p[0] = Node('function_definition', [p[1], p[2], p[3], p[4]])
#    pass

# Error rule for syntax errors
#def p_error(p):
 #   print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

fd = open(sys.argv[1], 'r')
#file_name = sys.argv[1]
data = fd.read()
print data
fd.close

result = parser.parse(data)
graph = result.makegraphicaltree()
#file_name = "tree_" + file_name
graph.write_pdf("tree")
'''
while True:
    try:
        s = input('calc > ')   # Use raw_input on Python 2
        print s
    except EOFError:
        break
    parser.parse(s)
'''
