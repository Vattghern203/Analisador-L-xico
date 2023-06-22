import ply.lex as lex
import ply.yacc as yacc

# Token list
tokens = [
    'VAR',
    'ID',
    'TIPO',
    'INTEIRO',
    'CADEIA_CAR',
    'ABRE_COLCH',
    'FECHA_COLCH',
    'ABRE_CHAV',
    'FECHA_CHAV',
    'VIRG',
    'PONTO_VIRG',
    'ABRE_PAR',
    'FECHA_PAR',
    'OPER_RELA',
    'OPER_MAT',
    'ITERADORES',
    'NEGACAO',
    'OPER_LOG',
    'NOME_FUNK',
    'COMENTARIO',
    'STR_INCOMPLETA',
    'VAR_ERRO',
    'NUM_ERRO',
    'INT_LITERAL',
    'STRING_LITERAL',
    'SE',
    'SENAO',
    'ENQUANTO',
    'LEIA',
    'ESCREVA',
    'PARA',
    'FUNK',
    'RETORNA',
    'IFSULDEMINAS',
    'INICIO',
    'COMPILADORES',
    'FIM',
    'INT',
    'REAL',
    'BOOLEANO',
    'TEXTO'
]

# Token regular expressions
t_VAR = r'[a-zA-Z]+\d\w'
t_INTEIRO = r'[+-]?\d+'
t_CADEIA_CAR = r'"[^"]+"'
t_ABRE_COLCH = r'\['
t_FECHA_COLCH = r'\]'
t_ABRE_CHAV = r'{'
t_FECHA_CHAV = r'}'
t_VIRG = r','
t_PONTO_VIRG = r';'
t_ABRE_PAR = r'\('
t_FECHA_PAR = r'\)'
t_OPER_RELA = r'==|!=|<=|>=|<|>'
t_OPER_MAT = r'\+|-|\*|/|%'
t_ITERADORES = r'ate|passo'
t_NEGACAO = r'!'
t_OPER_LOG = r'&&|\|\|'
t_NOME_FUNK = r'[a-zA-Z]\w*\([^)]*\)'
t_COMENTARIO = r'\#.*'
t_STR_INCOMPLETA = r'"[^"]*'
t_VAR_ERRO = r'\d+[a-zA-Z]+|[@!#$%&]+[a-zA-Z]+|[a-zA-Z]+\.\d+|[a-zA-Z]+[@!#$%&*]+'
t_NUM_ERRO = r'\d+\.\d*[a-zA-Z]+|\d+\.\d+|\d+\.\d*[a-zA-Z]+'
t_SE = r'\bse\b'
t_SENAO = r'\bsenao\b'
t_ENQUANTO = r'\benquanto\b'
t_LEIA = r'\bleia\b'
t_ESCREVA = r'\bescreva\b'
t_PARA = r'\bpara\b'
t_FUNK = r'\bfunk\b'
t_RETORNA = r'\bretorna\b'
t_IFSULDEMINAS = r'\bifsuldeminas\b'
t_INICIO = r'\binicio\b'
t_COMPILADORES = r'\bcompiladores\b'
t_FIM = r'\bfim\b'
t_INT = r'\bint\b'
t_REAL = r'[+-]?\d+\.\d+|\d+\.\d+'
t_BOOLEANO = r'\bbool\b'
t_TEXTO = r'\btexto\b'

# Ignored characters
t_ignore = ' \t'

# Newline tracking
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handling
def t_error(t):
    print(f"Invalid character '{t.value[0]}' at line {t.lineno}, position {find_column(t.lexer.lexdata, t)}")
    t.lexer.skip(1)

# Helper function to calculate column position
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return token.lexpos - line_start + 1

# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_program(p):
    '''
    program : stmt_list
    '''

def p_stmt_list(p):
    '''
    stmt_list : stmt
              | stmt_list stmt
    '''

def p_stmt(p):
    '''
    stmt : ID PONTO_VIRG
         | TIPO ID INTEIRO PONTO_VIRG
         | TIPO ID REAL PONTO_VIRG
         | TIPO ID CADEIA_CAR PONTO_VIRG
         | TIPO ID TEXTO PONTO_VIRG
         | se_stmt
    '''

def p_se_stmt(p):
    '''
    se_stmt : SE ABRE_PAR expr FECHA_PAR ABRE_CHAV stmt_list FECHA_CHAV
        | SE ABRE_PAR expr FECHA_PAR ABRE_CHAV stmt_list FECHA_CHAV SENAO ABRE_CHAV stmt_list FECHA_CHAV

    '''

def p_expr(p):
    '''
    expr : ID OPER_RELA ID
         | expr OPER_LOG expr
         | NEGACAO expr
    '''

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {find_column(p.lexer.lexdata, p)}")
    else:
        print("Syntax error: Unexpected end of input")

# Build the parser
parser = yacc.yacc()

# Test the parser
data = '''
texto nome = 'sergio';

leia(nome);

se (nome != "Wallace"){
    escreva("Nome incorreto, tente novamente");
}
senao {
    escreva("Parabens voce acertou o nome @@@$$");
}
'''

parser.parse(data, lexer=lexer)
