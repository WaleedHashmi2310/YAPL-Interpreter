import ply.lex as lex

tokens = [
    'DO',
    'WHILE',
    'LBRACE',
    'RBRACE',
    'SLICE',
    'PUSH',
    'INDEX',
    'POP',
    'DOT',
    'RBRACKET',
    'LBRACKET',
    'PRINT',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'NOTEQUAL',
    'EQUALEQUAL',
    'GT',
    'LT',
    'GTE',
    'LTE',
    'NOT',
    'AND',
    'OR',
    'INT',
    'FLOAT',
    'CHAR',
    'STRING',
    'BOOL',
    'LIST_t',
    'INT_t',
    'FLOAT_t',
    'CHAR_t',
    'STRING_t',
    'BOOL_t',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'POWER',
    'MODULUS',
    'INCREMENT',
    'DECREMENT',
    'EQUALS',
]

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_POWER = r'\^'
t_MODULUS = r'\%'
t_EQUALS = r'\='
t_ignore = ' \n'

def t_DO(t):
    r'do'
    t.type = 'DO'
    return t

def t_WHILE(t):
    r'while'
    t.type = 'WHILE'
    return t

def t_LBRACE(t):
    r'\{'
    t.type = 'LBRACE'
    return t

def t_RBRACE(t):
    r'\}'
    t.type = 'RBRACE'
    return t

def t_SLICE(t):
    r'slice'
    t.type = 'SLICE'
    return t

def t_PUSH(t):
    r'push'
    t.type = 'PUSH'
    return t

def t_INDEX(t):
    r'index'
    t.type = 'INDEX'
    return t

def t_POP(t):
    r'pop'
    t.type = 'POP'
    return t

def t_DOT(t):
    r'\.'
    t.type = 'DOT'
    return t

def t_LIST_t(t):
    r'list'
    t.type = 'LIST_t'
    return t

def t_RBRACKET(t):
    r'\]'
    t.type = 'RBRACKET'
    return t

def t_LBRACKET(t):
    r'\['
    t.type = 'LBRACKET'
    return t

def t_COMMA(t):
    r'\,'
    t.type = 'COMMA'
    return t

def t_LPAREN(t):
    r'\('
    t.type = 'LPAREN'
    return t

def t_RPAREN(t):
    r'\)'
    t.type = 'RPAREN'
    return t

def t_GTE(t):
    r'\>\='
    t.type = 'GTE'
    return t

def t_LTE(t):
    r'\<\='
    t.type = 'LTE'
    return t

def t_NOTEQUAL(t):
    r'\!\='
    t.type = 'NOTEQUAL'
    return t

def t_EQUALEQUAL(t):
    r'\=\='
    t.type = 'EQUALEQUAL'
    return t

def t_GT(t):
    r'\>'
    t.type = 'GT'
    return t

def t_LT(t):
    r'\<'
    t.type = 'LT'
    return t

def t_NOT(t):
    r'not'
    t.type = 'NOT'
    return t

def t_AND(t):
    r'and'
    t.type = 'AND'
    return t

def t_OR(t):
    r'or'
    t.type = 'OR'
    return t
    
def t_INCREMENT(t):
    r'\+\+'
    t.type = 'INCREMENT'
    return t

def t_DECREMENT(t):
    r'\-\-'
    t.type = 'DECREMENT'
    return t

def t_PRINT(t):
    r'print'
    t.type = 'PRINT'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r'"[a-zA-Z0-9]"'
    t.value= str(t.value[1:-1])
    t.type = 'CHAR'
    return t

def t_BOOL(t):
    r'True|False'
    if(t.value=='True'):
        t.value=bool(t.value)
    else:
        t.value=not bool(t.value)
    return t

def t_STRING(t):
    r'"[^"\n]*"'
    t.value= str(t.value[1:-1])
    t.type='STRING'
    return t

def t_INT_t(t):
    r'int'
    t.type = 'INT_t'
    return t

def t_FLOAT_t(t):
    r'float'
    t.type = 'FLOAT_t'
    return t

def t_CHAR_t(t):
    r'char'
    t.type = 'CHAR_t'
    return t

def t_BOOL_t(t):
    r'bool'
    t.type = 'BOOL_t'
    return t

def t_STRING_t(t):
    r'string'
    t.type = 'STRING_t'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal Characters")
    t.lexer.skip(1)