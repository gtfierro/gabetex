#!/usr/bin/env Python
import ply.lex as lex

tokens = (
		'NUMBER',
		'VARIABLE',
		'PLUS',
		'MINUS',
		'TIMES',
		'DIVIDE',
		'POWER',
		'INTEGRAL',
		'PHRASE',
		'LPAREN',
		'RPAREN',
		'DELIM',
		'LINE',
		)

t_NUMBER = r'\d+'
t_VARIABLE = r'\w'
t_PLUS = r'\+|plus'
t_MINUS = r'-|minus'
t_TIMES = r'\*|times'
t_DIVIDE = r'/'
t_POWER  = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DELIM = r'\$'
t_LINE	= r'\$[^\$]+\$'

def t_PHRASE(t):
	r'[^\$](?P<phrase>[\D\s[^\(\)]]+)\W'
	value = t.value.rstrip()
	if value == 'divided by':
		t.type = 'DIVIDE'
	elif value == 'multiplied by':
		t.type = 'TIMES'
	elif value == 'added to':
		t.type = 'PLUS'
	elif value == 'to the power of':
		t.type = 'POWER'
	return t

t_ignore  = ' \t\n'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == "__main__":
	data = '''
	( 3+4 )
	'''

	lexer.input(data.strip())

	while True:
		tok = lexer.token()
		if not tok: break
		print tok