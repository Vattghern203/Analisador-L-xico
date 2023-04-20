# -----------------------------------------------------------------------------
# example.py
#
# Example of using PLY To parse the following simple grammar.
#
#   expression : term PLUS term
#              | term MINUS term
#              | term
#
#   term       : factor TIMES factor
#              | factor DIVIDE factor
#              | factor
#
#   factor     : NUMBER
#              | NAME
#              | PLUS factor
#              | MINUS factor
#              | LPAREN expression RPAREN
#
# -----------------------------------------------------------------------------

from ply.lex import lex
from ply.yacc import yacc

# --- Tokenizer

# All tokens must be named in advance.
tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NAME',
    'NUMBER',
    'TIPO',
    'INTEIRO',
    'REAL',
    'CADEIA_CAR',
    'PARA',
    'SE',
    'SENAO',
    'ENQUANTO',
    'ESCREVA',
    'LEIA',
    'EQUALS',
    'COMMA',
    'COLON',
    'AND',
    'OR',
    'NOT',
    'LT',
    'GT',
    'LE',
    'GE',
    'NE',
)

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_TIPO = r'int|real|texto|bool'
t_INTEIRO = r'([+-])?\d+'
t_REAL = r'(([+-])?\d+)[.]\d+'
t_CADEIA_CAR = r'".*?"'
t_PARA = r'para'
t_SE = r'se'
t_SENAO = r'senao'
t_ENQUANTO = r'enquanto'
t_ESCREVA = r'escreva'
t_LEIA = r'leia'
t_EQUALS = r'=='
t_COMMA = r','
t_COLON = r':'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_NE = r'!='

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored token with an action associated with it
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handler for illegal characters
def t_error(t):
    last_newline_index = t.lexer.lexdata.rfind('\n', 0, t.lexpos)
    line = t.lexer.lineno
    column = t.lexpos - last_newline_index
    print(f"Line {line}, column {column}: Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()
    
# --- Parser

# Write functions for each grammar rule which is
# specified in the docstring.
def p_expression_binop(p):
    '''
    expression : term PLUS term
               | term MINUS term
               | term TIMES term
               | term DIVIDE term
               | term LT term
               | term GT term
               | term LE term
               | term GE term
               | term NE term
               | term AND term
               | term OR term
    '''
    p[0] = ('binop', p[2], p[1], p[3])


def p_expression_term(p):
    '''
    expression : term
    '''
    p[0] = p[1]

def p_term(p):
    '''
    term : factor TIMES factor
         | factor DIVIDE factor
    '''
    p[0] = ('binop', p[2], p[1], p[3])

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor_number(p):
    '''
    factor : NUMBER
    '''
    p[0] = ('number', p[1])

def p_factor_name(p):
    '''
    factor : NAME
    '''
    p[0] = ('name', p[1])

def p_factor_unary(p):
    '''
    factor : PLUS factor
           | MINUS factor
    '''
    p[0] = ('unary', p[1], p[2])

def p_factor_grouped(p):
    '''
    factor : LPAREN expression RPAREN
    '''
    p[0] = ('grouped', p[2])

def p_factor_string(p):
    '''
    factor : CADEIA_CAR
    '''
    p[0] = ('string', p[1])

def p_factor_define(p):
    '''
    factor : EQUALS
    '''
    p[0] = ('equals', p[1])

def p_factor_type(p):
    '''
    factor : TIPO
    '''
    p[0] = ('type', p[1])

def p_error(p):
    line = p.lineno
    column = p.lexpos - lexer.lexdata.rfind('\n', 0, p.lexpos)
    print(f"Syntax error at line {line}, column {column}: {p.value!r}")


# Build the parser
parser = yacc()

# Parse an expression
ast = parser.parse('escreva')

print(ast)