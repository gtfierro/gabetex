#!/usr/bin/env Python
import ply.yacc as yacc
from latokens import tokens

names = { }

def p_latex(p):
	'''latex		:	expression'''
	p[0] = '$'+p[1]+'$'
	
def p_expression(p):
	'''expression	: DELIM expression DELIM
					| expression PLUS term
					| expression MINUS term
					| term'''
					
	if len(p) == 2:
		p[0] = p[1]
	elif len(p) == 4:
		if p[2] == '+'	:	p[0] = p[1] + '+' + p[3]
		elif p[2] == '-':	p[0] = p[1] + '-' + p[3]

		
def p_term(p):
	'''term			:	term TIMES factor
					|	term DIVIDE factor
					|	factor'''
	print p[:]
	if len(p) == 4:
		if p[2] == '*'		:	p[0] = p[1] + '\cdot ' + p[3]
		elif p[2] == '/'	:	p[0] = '\\frac{'+p[1] + '}{' + p[3]+'}'
	elif len(p) == 2:
		p[0] = p[1]
	print p[:]
			
def p_factor(p):
	'''factor		:	NUMBER
					|	VARIABLE
					|	LPAREN expression RPAREN'''
	print p[:]	
	if len(p) == 2:				
		p[0] = p[1]
	elif len(p) == 4:
		if p[1] == '(':	p[0] = '('+p[2]+')'	
	print p[:]
def p_error(p):
    print "Syntax error in input!"

parser = yacc.yacc()

while True:
   try:
       s = raw_input('parse > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s,debug=True)
   print result