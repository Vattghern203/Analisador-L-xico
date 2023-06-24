from lark import Lark, UnexpectedToken, UnexpectedCharacters, UnexpectedEOF, UnexpectedInput, Token

grammar = '''
    start: ifsuldeminas compiladores inicio codigos fim
    ifsuldeminas: "IFSULDEMINAS"
    compiladores: "COMPILADORES"
    inicio: "INICIO"
    fim: "FIM"
    codigos: codigo+
    codigo: (logico | relacional | expressao_interna | para | enquanto | definir_funk | condicional) | (variavel | matematica | escreva | leia | chamar_funk | retorno | reatribuir) PONTO_VIRG 
    variavel: tipo VAR "=" (operacao | LITERAL | VAR )
    matematica: operacao+
    tipo: "INT" | "REAL" | "BOOLEANO" | "TEXTO"
    operacao: LITERAL OPER_MAT LITERAL | varmat OPER_MAT varmat | varmat OPER_MAT LITERAL | LITERAL OPER_MAT varmat
    varmat:VAR REAL | VAR INTEIRO | VAR | LITERAL
    logico: VAR OPER_LOG VAR | VAR OPER_LOG CADEIA_CAR | VAR OPER_LOG LITERAL | LITERAL OPER_LOG VAR | VAR OPER_LOG BOOLEANO
    relacional: VAR OPER_RELA VAR | VAR OPER_RELA LITERAL | LITERAL OPER_RELA VAR | LITERAL OPER_RELA LITERAL
    expressao_interna: ABRE_CHAV codigos FECHA_CHAV
    para: "PARA" ABRE_PAR (VAR "=" LITERAL | variavel) PONTO_VIRG relacional PONTO_VIRG VAR ITERADORES FECHA_PAR expressao_interna
    condicional: "SE" ABRE_PAR relacional FECHA_PAR expressao_interna | "SE" ABRE_PAR logico relacional FECHA_PAR expressao_interna | "SE" ABRE_PAR relacional FECHA_PAR expressao_interna "SENAO" expressao_interna | "SE" ABRE_PAR logico FECHA_PAR expressao_interna "SENAO" expressao_interna
    enquanto: "ENQUANTO" ABRE_PAR relacional FECHA_PAR expressao_interna | "ENQUANTO" ABRE_PAR BOOLEANO FECHA_PAR expressao_interna
    retorno: "RETORNO" (VAR | LITERAL | chamar_funk )
    definir_funk: "FUNK" NOME_FUNK "(" VAR |  ")" expressao_interna
    chamar_funk: NOME_FUNK "(" ")"
    escreva: "ESCREVA" ABRE_PAR CADEIA_CAR FECHA_PAR | "ESCREVA" ABRE_PAR (CADEIA_CAR | VAR) FECHA_PAR | "ESCREVA" ABRE_PAR VAR FECHA_PAR | "ESCREVA" ABRE_PAR CADEIA_CAR INTEIRO FECHA_PAR | "ESCREVA" ABRE_PAR INTEIRO FECHA_PAR | "ESCREVA" ABRE_PAR CADEIA_CAR REAL FECHA_PAR | "ESCREVA" ABRE_PAR REAL FECHA_PAR
    leia: "LEIA" ABRE_PAR VAR FECHA_PAR
    LITERAL: INTEIRO | REAL | CADEIA_CAR
    reatribuir: VAR "=" ((LITERAL | VAR) OPER_MAT (LITERAL | VAR)) | LITERAL | VAR

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
IFSULDEMINAS
COMPILADORES

INICIO

FUNK fatorial(n){
	INT resultado = 1;
	INT i = 10;
	PARA(i = 1; i <= n; i++){
		resultado = resultado * i;
	}
		RETORNO resultado;
}

FIM
'''

def errorHandling():
    return True

# Create the Lark parser
parser = Lark(grammar, start='start')

# Parse the input string

try:
    tree = parser.parse(input_string)

    print(tree.pretty())

except UnexpectedCharacters as err:

    print(err)