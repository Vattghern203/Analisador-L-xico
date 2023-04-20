
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CADEIA_CAR COLON COMMA DIVIDE ENQUANTO EQUALS ESCREVA GE GT INTEIRO LE LEIA LPAREN LT MINUS NAME NE NOT NUMBER OR PARA PLUS REAL RPAREN SE SENAO TIMES TIPO\n    expression : term PLUS term\n               | term MINUS term\n               | term TIMES term\n               | term DIVIDE term\n               | term LT term\n               | term GT term\n               | term LE term\n               | term GE term\n               | term NE term\n               | term AND term\n               | term OR term\n    \n    expression : term\n    \n    term : factor TIMES factor\n         | factor DIVIDE factor\n    \n    term : factor\n    \n    factor : NUMBER\n    \n    factor : NAME\n    \n    factor : PLUS factor\n           | MINUS factor\n    \n    factor : LPAREN expression RPAREN\n    \n    factor : CADEIA_CAR\n    \n    factor : EQUALS\n    \n    factor : TIPO\n    '
    
_lr_action_items = {'NUMBER':([0,3,4,8,12,13,14,15,16,17,18,19,20,21,22,25,26,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'NAME':([0,3,4,8,12,13,14,15,16,17,18,19,20,21,22,25,26,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'PLUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,39,40,41,],[3,12,3,3,-15,-16,-17,3,-21,-22,-23,3,3,3,3,3,3,3,3,3,3,3,-18,-19,3,3,-13,-14,-20,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,39,40,41,],[4,13,4,4,-15,-16,-17,4,-21,-22,-23,4,4,4,4,4,4,4,4,4,4,4,-18,-19,4,4,-13,-14,-20,]),'LPAREN':([0,3,4,8,12,13,14,15,16,17,18,19,20,21,22,25,26,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'CADEIA_CAR':([0,3,4,8,12,13,14,15,16,17,18,19,20,21,22,25,26,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'EQUALS':([0,3,4,8,12,13,14,15,16,17,18,19,20,21,22,25,26,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'TIPO':([0,3,4,8,12,13,14,15,16,17,18,19,20,21,22,25,26,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'$end':([1,2,5,6,7,9,10,11,23,24,28,29,30,31,32,33,34,35,36,37,38,39,40,41,],[0,-12,-15,-16,-17,-21,-22,-23,-18,-19,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-13,-14,-20,]),'TIMES':([2,5,6,7,9,10,11,23,24,39,40,41,],[14,25,-16,-17,-21,-22,-23,-18,-19,-13,-14,-20,]),'DIVIDE':([2,5,6,7,9,10,11,23,24,39,40,41,],[15,26,-16,-17,-21,-22,-23,-18,-19,-13,-14,-20,]),'LT':([2,5,6,7,9,10,11,23,24,39,40,41,],[16,-15,-16,-17,-21,-22,-23,-18,-19,-13,-14,-20,]),'GT':([2,5,6,7,9,10,11,23,24,39,40,41,],[17,-15,-16,-17,-21,-22,-23,-18,-19,-13,-14,-20,]),'LE':([2,5,6,7,9,10,11,23,24,39,40,41,],[18,-15,-16,-17,-21,-22,-23,-18,-19,-13,-14,-20,]),'GE':([2,5,6,7,9,10,11,23,24,39,40,41,],[19,-15,-16,-17,-21,-22,-23,-18,-19,-13,-14,-20,]),'NE':([2,5,6,7,9,10,11,23,24,39,40,41,],[20,-15,-16,-17,-21,-22,-23,-18,-19,-13,-14,-20,]),'AND':([2,5,6,7,9,10,11,23,24,39,40,41,],[21,-15,-16,-17,-21,-22,-23,-18,-19,-13,-14,-20,]),'OR':([2,5,6,7,9,10,11,23,24,39,40,41,],[22,-15,-16,-17,-21,-22,-23,-18,-19,-13,-14,-20,]),'RPAREN':([2,5,6,7,9,10,11,23,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,],[-12,-15,-16,-17,-21,-22,-23,-18,-19,41,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-13,-14,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,8,],[1,27,]),'term':([0,8,12,13,14,15,16,17,18,19,20,21,22,],[2,2,28,29,30,31,32,33,34,35,36,37,38,]),'factor':([0,3,4,8,12,13,14,15,16,17,18,19,20,21,22,25,26,],[5,23,24,5,5,5,5,5,5,5,5,5,5,5,5,39,40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> term PLUS term','expression',3,'p_expression_binop','main.py',122),
  ('expression -> term MINUS term','expression',3,'p_expression_binop','main.py',123),
  ('expression -> term TIMES term','expression',3,'p_expression_binop','main.py',124),
  ('expression -> term DIVIDE term','expression',3,'p_expression_binop','main.py',125),
  ('expression -> term LT term','expression',3,'p_expression_binop','main.py',126),
  ('expression -> term GT term','expression',3,'p_expression_binop','main.py',127),
  ('expression -> term LE term','expression',3,'p_expression_binop','main.py',128),
  ('expression -> term GE term','expression',3,'p_expression_binop','main.py',129),
  ('expression -> term NE term','expression',3,'p_expression_binop','main.py',130),
  ('expression -> term AND term','expression',3,'p_expression_binop','main.py',131),
  ('expression -> term OR term','expression',3,'p_expression_binop','main.py',132),
  ('expression -> term','expression',1,'p_expression_term','main.py',139),
  ('term -> factor TIMES factor','term',3,'p_term','main.py',145),
  ('term -> factor DIVIDE factor','term',3,'p_term','main.py',146),
  ('term -> factor','term',1,'p_term_factor','main.py',152),
  ('factor -> NUMBER','factor',1,'p_factor_number','main.py',158),
  ('factor -> NAME','factor',1,'p_factor_name','main.py',164),
  ('factor -> PLUS factor','factor',2,'p_factor_unary','main.py',170),
  ('factor -> MINUS factor','factor',2,'p_factor_unary','main.py',171),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_grouped','main.py',177),
  ('factor -> CADEIA_CAR','factor',1,'p_factor_string','main.py',183),
  ('factor -> EQUALS','factor',1,'p_factor_define','main.py',189),
  ('factor -> TIPO','factor',1,'p_factor_type','main.py',195),
]