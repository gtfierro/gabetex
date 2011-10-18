#!/usr/bin/env Python
import ply.yacc as yacc
from latokens import tokens

names = { }

def p_statement_expr(p):
	'statement : LINE'
	print(p[1])

def p_expression_binop(p):
	'''statement	:	expression PLUS expression
					|	expression MINUS expression
					|	expression TIMES expression
					|	expression DIVIDE expression
					|	expression POWER expression'''
	if p[2] == '+'	:	p[0] = '$'+p[1]+'+'+p[3]+'$'
	elif p[2] == '-':	p[0] = '$'+p[1]+'-'+p[3]+'$'
	elif p[2] == '*':	p[0] = '$'+p[1]+'\cdot'+p[3]+'$'
	elif p[2] == '/':	p[0] = '$\\frac{'+p[1]+'}{'+p[3]+'}$'
	elif p[2] == '^':	p[0] = '$'+p[1]+'^{'+p[3]+'}$'
	
def p_expression(p):
	'''expression	:	LPAREN	expression	RPAREN
					|	NUMBER'''
	if len(p) == 4:
		p[0] = '('+p[2]+')'
	elif len(p) == 2:
		p[0] = p[1]
	
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