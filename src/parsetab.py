
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE LPAREN MINUS NAME NUMBER PLUS RPAREN TIMES\n    expression : term PLUS term\n               | term MINUS term\n    \n    expression : term\n    \n    term : factor TIMES factor\n         | factor DIVIDE factor\n    \n    term : factor\n    \n    factor : NUMBER\n    \n    factor : NAME\n    \n    factor : PLUS factor\n           | MINUS factor\n    \n    factor : LPAREN expression RPAREN\n    '
    
_lr_action_items = {'NUMBER':([0,3,4,8,9,10,13,14,],[6,6,6,6,6,6,6,6,]),'NAME':([0,3,4,8,9,10,13,14,],[7,7,7,7,7,7,7,7,]),'PLUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,19,20,],[3,9,3,3,-6,-7,-8,3,3,3,-9,-10,3,3,-4,-5,-11,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,18,19,20,],[4,10,4,4,-6,-7,-8,4,4,4,-9,-10,4,4,-4,-5,-11,]),'LPAREN':([0,3,4,8,9,10,13,14,],[8,8,8,8,8,8,8,8,]),'$end':([1,2,5,6,7,11,12,16,17,18,19,20,],[0,-3,-6,-7,-8,-9,-10,-1,-2,-4,-5,-11,]),'RPAREN':([2,5,6,7,11,12,15,16,17,18,19,20,],[-3,-6,-7,-8,-9,-10,20,-1,-2,-4,-5,-11,]),'TIMES':([5,6,7,11,12,20,],[13,-7,-8,-9,-10,-11,]),'DIVIDE':([5,6,7,11,12,20,],[14,-7,-8,-9,-10,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,8,],[1,15,]),'term':([0,8,9,10,],[2,2,16,17,]),'factor':([0,3,4,8,9,10,13,14,],[5,11,12,5,5,5,18,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> term PLUS term','expression',3,'p_expression','main.py',69),
  ('expression -> term MINUS term','expression',3,'p_expression','main.py',70),
  ('expression -> term','expression',1,'p_expression_term','main.py',81),
  ('term -> factor TIMES factor','term',3,'p_term','main.py',87),
  ('term -> factor DIVIDE factor','term',3,'p_term','main.py',88),
  ('term -> factor','term',1,'p_term_factor','main.py',94),
  ('factor -> NUMBER','factor',1,'p_factor_number','main.py',100),
  ('factor -> NAME','factor',1,'p_factor_name','main.py',106),
  ('factor -> PLUS factor','factor',2,'p_factor_unary','main.py',112),
  ('factor -> MINUS factor','factor',2,'p_factor_unary','main.py',113),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_grouped','main.py',119),
]
