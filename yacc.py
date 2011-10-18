#!/usr/bin/env Python
import ply.yacc as yacc
from latokens import tokens

names = { }

def p_statement(p):
	'''statement	:	expression'''
	if len(p) == 2:
		p[0] = '$'+p[1]+'$'
	
def p_expression_binop(p):
	'''expression	:	expression PLUS term
					|	expression MINUS term
					|	expression TIMES term
					|	expression DIVIDE term
					|	expression POWER term
					|	term'''
	print(len(p))
	if 	 p[2] == '+':	p[0] = '$'+p[1]+'+'+p[3]+'$'
	elif p[2] == '-':	p[0] = '$'+p[1]+'-'+p[3]+'$'
	elif p[2] == '*':	p[0] = '$'+p[1]+'\cdot'+p[3]+'$'
	elif p[2] == '/':	p[0] = '$\\frac{'+p[1]+'}{'+p[3]+'}$'
	elif p[2] == '^':	p[0] = '$'+p[1]+'^{'+p[3]+'}$'

		
def p_term(p):
	'''term			:	NUMBER
					|	VARIABLE
					|	LINE
					|	LPAREN expression RPAREN'''
	if '$' in p:
		p[0] = p[0][1:-1]
	elif len(p) == 4:
		p[0] = '$('+p[2]+')$'

def p_error(p):
    print "Syntax error in input!"

parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print result