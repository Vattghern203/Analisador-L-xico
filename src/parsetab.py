
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CHAV ABRE_COLCH ABRE_PAR BOOLEANO CADEIA_CAR COMENTARIO COMPILADORES ENQUANTO ESCREVA FECHA_CHAV FECHA_COLCH FECHA_PAR FIM FUNK ID IFSULDEMINAS INICIO INT INTEIRO INT_LITERAL ITERADORES LEIA NEGACAO NOME_FUNK NUM_ERRO OPER_LOG OPER_MAT OPER_RELA PARA PONTO_VIRG REAL RETORNA SE SENAO STRING_LITERAL STR_INCOMPLETA TEXTO TIPO VAR VAR_ERRO VIRG\n    program : stmt_list\n    \n    stmt_list : stmt\n              | stmt_list stmt\n    \n    stmt : ID PONTO_VIRG\n         | TIPO ID INTEIRO PONTO_VIRG\n         | TIPO ID REAL PONTO_VIRG\n         | TIPO ID CADEIA_CAR PONTO_VIRG\n         | TIPO ID TEXTO PONTO_VIRG\n         | se_stmt\n    \n    se_stmt : SE ABRE_PAR expr FECHA_PAR ABRE_CHAV stmt_list FECHA_CHAV\n        | SE ABRE_PAR expr FECHA_PAR ABRE_CHAV stmt_list FECHA_CHAV SENAO ABRE_CHAV stmt_list FECHA_CHAV\n\n    \n    expr : ID OPER_RELA ID\n         | expr OPER_LOG expr\n         | NEGACAO expr\n    '
    
_lr_action_items = {'ID':([0,2,3,5,6,8,9,11,18,19,20,21,22,24,25,27,30,31,33,34,35,],[4,4,-2,10,-9,-3,-4,17,17,-5,-6,-7,-8,17,29,4,4,-10,4,4,-11,]),'TIPO':([0,2,3,6,8,9,19,20,21,22,27,30,31,33,34,35,],[5,5,-2,-9,-3,-4,-5,-6,-7,-8,5,5,-10,5,5,-11,]),'SE':([0,2,3,6,8,9,19,20,21,22,27,30,31,33,34,35,],[7,7,-2,-9,-3,-4,-5,-6,-7,-8,7,7,-10,7,7,-11,]),'$end':([1,2,3,6,8,9,19,20,21,22,31,35,],[0,-1,-2,-9,-3,-4,-5,-6,-7,-8,-10,-11,]),'FECHA_CHAV':([3,6,8,9,19,20,21,22,30,31,34,35,],[-2,-9,-3,-4,-5,-6,-7,-8,31,-10,35,-11,]),'PONTO_VIRG':([4,12,13,14,15,],[9,19,20,21,22,]),'ABRE_PAR':([7,],[11,]),'INTEIRO':([10,],[12,]),'REAL':([10,],[13,]),'CADEIA_CAR':([10,],[14,]),'TEXTO':([10,],[15,]),'NEGACAO':([11,18,24,],[18,18,18,]),'FECHA_PAR':([16,26,28,29,],[23,-14,-13,-12,]),'OPER_LOG':([16,26,28,29,],[24,24,24,-12,]),'OPER_RELA':([17,],[25,]),'ABRE_CHAV':([23,32,],[27,33,]),'SENAO':([31,],[32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,27,33,],[2,30,34,]),'stmt':([0,2,27,30,33,34,],[3,8,3,8,3,8,]),'se_stmt':([0,2,27,30,33,34,],[6,6,6,6,6,6,]),'expr':([11,18,24,],[16,26,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list','program',1,'p_program','main.py',112),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','main.py',117),
  ('stmt_list -> stmt_list stmt','stmt_list',2,'p_stmt_list','main.py',118),
  ('stmt -> ID PONTO_VIRG','stmt',2,'p_stmt','main.py',123),
  ('stmt -> TIPO ID INTEIRO PONTO_VIRG','stmt',4,'p_stmt','main.py',124),
  ('stmt -> TIPO ID REAL PONTO_VIRG','stmt',4,'p_stmt','main.py',125),
  ('stmt -> TIPO ID CADEIA_CAR PONTO_VIRG','stmt',4,'p_stmt','main.py',126),
  ('stmt -> TIPO ID TEXTO PONTO_VIRG','stmt',4,'p_stmt','main.py',127),
  ('stmt -> se_stmt','stmt',1,'p_stmt','main.py',128),
  ('se_stmt -> SE ABRE_PAR expr FECHA_PAR ABRE_CHAV stmt_list FECHA_CHAV','se_stmt',7,'p_se_stmt','main.py',133),
  ('se_stmt -> SE ABRE_PAR expr FECHA_PAR ABRE_CHAV stmt_list FECHA_CHAV SENAO ABRE_CHAV stmt_list FECHA_CHAV','se_stmt',11,'p_se_stmt','main.py',134),
  ('expr -> ID OPER_RELA ID','expr',3,'p_expr','main.py',140),
  ('expr -> expr OPER_LOG expr','expr',3,'p_expr','main.py',141),
  ('expr -> NEGACAO expr','expr',2,'p_expr','main.py',142),
]
