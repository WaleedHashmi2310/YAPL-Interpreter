import ply.yacc as yacc
import sys
from lexer import tokens


precedence = (
    
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUALEQUAL', 'NOTEQUAL'),
    ('left', 'GT', 'LT', 'GTE', 'LTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('left', 'MODULUS', 'POWER'),
    ('right', 'NOT')
)

def p_calc(p):
    '''
    calc : expression
         | empty
         | var_declare
         | var_assign
         | incdec
    '''
    p[0] = p[1]

def p_lparen(p):
    '''
    lparen : LPAREN
    '''
    p[0] = p[1]

def p_rparen(p):
    '''
    rparen : RPAREN 
    '''
    p[0] = p[1]

def p_inc_dec(p):
    '''
    incdec : NAME INCREMENT
           | NAME DECREMENT
    '''
    p[0] = (p[2], p[1])

def p_inc_dec_empty(p):
    '''
    incdec :
    '''
    return None

def p_expression_empty(p):
    '''
    expression :
    '''
    return None


def p_expression_int_float_char_bool_string(p):
    '''
    expression : INT
               | FLOAT
               | CHAR
               | BOOL
               | STRING
    '''
    p[0] = p[1]


def p_expression_neg_name(p):
    '''
    expression : MINUS NAME
    '''
    p[0] = ('minus', p[2])


def p_expression_neg_expression(p):
    '''
    expression : MINUS expression
    '''
    p[0] = -p[2]

def p_expression_logic_not(p):
    '''
    expression : NOT expression
    '''
    p[0] = (p[1], p[2])

def p_expression_logic(p):
    '''
    expression : expression AND expression
               | expression OR expression
               | expression EQUALEQUAL expression
               | expression NOTEQUAL expression
               | expression GT expression
               | expression LT expression
               | expression GTE expression
               | expression LTE expression     
    '''
    p[0] = (p[1], p[2], p[3])

def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
               | expression POWER expression
               | expression MODULUS expression
    '''
    p[0] = (p[2],p[1],p[3])

def p_expression_parens(p):
    '''
    expression : lparen expression rparen
    '''
    p[0] = p[2]

def p_var_int_declare(p):
    '''
    var_declare : INT_t NAME EQUALS expression
    '''
    p[0] = (p[1],'=', p[2], p[4])
    
def p_var_float_declare(p):
    '''
    var_declare : FLOAT_t NAME EQUALS expression
    '''
    p[0] = (p[1],'=', p[2], p[4])

def p_var_char_declare(p):
    '''
    var_declare : CHAR_t NAME EQUALS expression
    '''
    p[0] = (p[1],'=', p[2], p[4])

def p_var_string_declare(p):
    '''
    var_declare : STRING_t NAME EQUALS expression
    '''
    p[0] = (p[1],'=', p[2], p[4])

def p_var_bool_declare(p):
    '''
    var_declare : BOOL_t NAME EQUALS expression
    '''
    p[0] = (p[1],'=', p[2], p[4])

def p_var_list_declare(p):
    '''
    var_declare : LIST_t NAME EQUALS LBRACKET expression RBRACKET
    '''
    p[0] = (p[1], '=', p[2], p[5])

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
    '''
    p[0] = ('=', p[1], p[3])

def p_var_access(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])

def p_expression_comma(p):
    '''
    expression : expression COMMA expression
    '''
    p[0] = (p[2],p[1],p[3])

def p_print_var(p):
    '''
    expression : PRINT lparen NAME rparen
    '''
    p[0] = ('print_var', p[3])

def p_print(p):
    '''
    expression : PRINT lparen expression rparen
    '''
    p[0] = ('print', p[3])

def p_slice(p):
    '''
    expression : NAME DOT SLICE LPAREN INT COMMA INT RPAREN
    '''
    p[0] = ('slice', p[1], p[5], p[7])

def p_push(p):
    '''
    expression : NAME DOT PUSH LPAREN expression RPAREN
    '''
    p[0] = ('push', p[1], p[5])

def p_index(p):
    '''
    expression : NAME DOT INDEX LPAREN INT RPAREN
    '''
    p[0] = ('index', p[1], p[5])

def p_legacy_index(p):
    '''
    expression : NAME LBRACKET INT RBRACKET
    '''
    p[0] = ('index', p[1], p[3])
    
def p_pop(p):
    '''
    expression : NAME DOT POP LPAREN INT RPAREN
    '''
    p[0] = ('pop', p[1], p[5])

def p_expression_do_while(p):
    '''
    expression : var_declare DO LBRACE expression incdec RBRACE WHILE LPAREN expression RPAREN
    '''
    p[0] = ('dowhile', p[1], p[4], p[5], p[9])

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
    print('Syntax Error')