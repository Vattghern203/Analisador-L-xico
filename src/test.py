import ply.lex as lex
import ply.yacc as yacc
from tkinter import Tk, Text, Button, filedialog

# List of tokens
tokens = [
    'VAR',
    'TIPO',
    'PONTO_VIRG',
    'SE',
    'ABRE_PAR',
    'OPER_RELA',
    'FECHA_PAR',
    'ABRE_CHAV',
    'FECHA_CHAV',
    'SENAO',
    'ENQUANTO',
    'PARA',
    'LEIA',
    'ESCREVA',
    'OPER_ATRIB_IGUAL',
    'NOME_FUNK',
]

# Token regular expressions
t_VAR = r'VAR'
t_TIPO = r'TIPO'
t_PONTO_VIRG = r'\;'
t_SE = r'SE'
t_ABRE_PAR = r'\('
t_OPER_RELA = r'OPER_RELA'
t_FECHA_PAR = r'\)'
t_ABRE_CHAV = r'\{'
t_FECHA_CHAV = r'\}'
t_SENAO = r'SENAO'
t_ENQUANTO = r'ENQUANTO'
t_PARA = r'PARA'
t_LEIA = r'LEIA'
t_ESCREVA = r'ESCREVA'
t_OPER_ATRIB_IGUAL = r'OPER_ATRIB_IGUAL'
t_NOME_FUNK = r'NOME_FUNK'

# Ignored characters
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Invalid token: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Grammar rules
def p_compiladores(p):
    '''compiladores : COMPILADORES'''

def p_inicio(p):
    '''inicio : INICIO'''

def p_codigos(p):
    '''codigos : codigos codigo
               | codigo'''

def p_codigo(p):
    '''codigo : decl_var
              | condicional
              | repeticao
              | leia
              | escreva
              | atribuicao
              | chamada_funk'''

def p_decl_var(p):
    '''decl_var : VAR VAR TIPO PONTO_VIRG'''

def p_condicional(p):
    '''condicional : SE ABRE_PAR VAR OPER_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
                   | SE ABRE_PAR VAR OPER_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV'''

def p_repeticao(p):
    '''repeticao : ENQUANTO ABRE_PAR VAR OPER_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV
                 | PARA ABRE_PAR VAR PONTO_VIRG VAR PONTO_VIRG VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV'''

def p_leia(p):
    '''leia : LEIA ABRE_PAR VAR FECHA_PAR PONTO_VIRG'''

def p_escreva(p):
    '''escreva : ESCREVA ABRE_PAR VAR FECHA_PAR PONTO_VIRG'''

def p_atribuicao(p):
    '''atribuicao : VAR OPER_ATRIB_IGUAL VAR PONTO_VIRG'''

def p_chamada_funk(p):
    '''chamada_funk : NOME_FUNK PONTO_VIRG'''

def p_error(p):
    if p:
        line = p.lineno
        print(f"Syntax error at line {line}")

# Build the parser
parser = yacc.yacc()

# Create the GUI
root = Tk()
root.geometry('500x500')
root.title("Compiladores")
root.resizable(False, False)

# Text area
text_area = Text(root, height=30, width=60)
text_area.pack()

# Open file function
def open_file():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    with open(file, 'r') as f:
        code = f.read()
        text_area.delete("1.0", "end")
        text_area.insert("1.0", code)

# Parse file function
def parse_file():
    code = text_area.get("1.0", "end-1c")
    lexer.input(code)
    result = parser.parse()
    if result is not None:
        print("Parsing completed successfully.")
    else:
        print("Parsing failed.")

# Buttons
open_button = Button(root, text="Open File", command=open_file)
open_button.pack()

parse_button = Button(root, text="Parse File", command=parse_file)
parse_button.pack()

root.mainloop()