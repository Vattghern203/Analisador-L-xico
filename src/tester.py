from lark import Lark

grammar = '''
    start: ifsuldeminas compiladores inicio codigos fim
    ifsuldeminas: "IFSULDEMINAS"
    compiladores: "COMPILADORES"
    inicio: "INICIO"
    fim: "FIM"
    codigos: codigo+
    codigo: (logico | relacional | expressao_interna | para | enquanto | retorno | definir_funk) | (variavel | matematica | escreva | leia | chamar_funk | condicional) PONTO_VIRG 
    variavel: tipo VAR "=" (operacao | LITERAL )
    matematica: operacao+
    tipo: "INT" | "REAL" | "BOOLEANO" | "CADEIA_CAR"
    operacao: INTEIRO OPER_MAT INTEIRO | varmat OPER_MAT varmat | varmat OPER_MAT INTEIRO | INTEIRO OPER_MAT varmat | REAL OPER_MAT REAL | varmat OPER_MAT REAL | REAL OPER_MAT varmat
    varmat: VAR INTEIRO | VAR REAL
    logico: VAR OPER_LOG VAR | VAR OPER_LOG CADEIA_CAR | VAR OPER_LOG INTEIRO | VAR OPER_LOG REAL | VAR OPER_LOG BOOLEANO
    relacional: VAR OPER_RELA VAR | VAR OPER_RELA LITERAL | LITERAL OPER_RELA VAR
    expressao_interna: ABRE_CHAV codigos FECHA_CHAV
    para: "PARA" ABRE_PAR (VAR "=" LITERAL | variavel) PONTO_VIRG relacional PONTO_VIRG VAR ITERADORES FECHA_PAR expressao_interna
    condicional: "SE" ABRE_PAR relacional FECHA_PAR expressao_interna | "SE" ABRE_PAR logico FECHA_PAR expressao_interna | "SE" ABRE_PAR relacional FECHA_PAR expressao_interna "SENAO" expressao_interna | "SE" ABRE_PAR logico FECHA_PAR expressao_interna "SENAO" expressao_interna
    enquanto: "ENQUANTO" ABRE_PAR relacional FECHA_PAR expressao_interna | "ENQUANTO" ABRE_PAR BOOLEANO FECHA_PAR expressao_interna
    retorno: "RETORNO" ABRE_PAR VAR FECHA_PAR | "RETORNO" INTEIRO
    definir_funk: "FUNK" NOME_FUNK "(" ")" expressao_interna
    chamar_funk: NOME_FUNK "(" ")"
    escreva: "ESCREVA" ABRE_PAR CADEIA_CAR FECHA_PAR | "ESCREVA" ABRE_PAR (CADEIA_CAR | VAR) FECHA_PAR | "ESCREVA" ABRE_PAR VAR FECHA_PAR | "ESCREVA" ABRE_PAR CADEIA_CAR INTEIRO FECHA_PAR | "ESCREVA" ABRE_PAR INTEIRO FECHA_PAR | "ESCREVA" ABRE_PAR CADEIA_CAR REAL FECHA_PAR | "ESCREVA" ABRE_PAR REAL FECHA_PAR
    leia: "LEIA" ABRE_PAR VAR FECHA_PAR
    LITERAL: INTEIRO | REAL | CADEIA_CAR

    ABRE_PAR: "("
    FECHA_PAR: ")"
    ABRE_CHAV: "{"
    FECHA_CHAV: "}"
    PONTO_VIRG: ";"
    INTEIRO: /-?\d+/
    REAL: /-?\d+\.\d+/
    VAR: /[a-zA-Z_]\w*/
    CADEIA_CAR: /".*?"/
    OPER_MAT: "+" | "-" | "*" | "/"
    OPER_LOG: "E" | "OU"
    OPER_RELA: "==" | "!=" | ">" | "<" | ">=" | "<="
    NOME_FUNK: /[a-zA-Z_]\w*/
    ITERADORES: "++" | "--"
    BOOLEANO: "VERDADEIRO" | "FALSO"

    %import common.WS
    %ignore WS
'''

input_string = '''
IFSULDEMINAS COMPILADORES
INICIO
ESCREVA("DRagon Ball");
INT num = 10;
PARA(INT i = 0; i < 10; i++) {
    ESCREVA("djavam");
}

LEIA();

FIM
'''

# Create the Lark parser
parser = Lark(grammar, start='start')

# Parse the input string
tree = parser.parse(input_string)
print(tree.pretty())
print("str =", input_string)
