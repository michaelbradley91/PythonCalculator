import ui
from py_expression_eval import Parser


def button_pressed(button: str):
	global clear_next
	if clear_next:
		clear_next = False
		output.text = ''
		
	output.text += button

def one_pressed(sender):
	button_pressed('1')

def two_pressed(sender):
	button_pressed('2')

def three_pressed(sender):
	button_pressed('3')

def four_pressed(sender):
	button_pressed('4')

def five_pressed(sender):
	button_pressed('5')
	
def six_pressed(sender):
	button_pressed('6')
	
def seven_pressed(sender):
	button_pressed('7')

def eight_pressed(sender):
	button_pressed('8')

def nine_pressed(sender):
	button_pressed('9')

def zero_pressed(sender):
	button_pressed('0')

def dot_pressed(sender):
	button_pressed('.')
	
def times_pressed(sender):
	button_pressed('*')

def divide_pressed(sender):
	button_pressed('/')

def plus_pressed(sender):
	button_pressed('+')

def minus_pressed(sender):
	button_pressed('-')

def power_pressed(sender):
	button_pressed('**')

def open_bracket_pressed(sender):
	button_pressed('(')

def close_bracket_pressed(sender):
	button_pressed(')')

def delete_pressed(sender):
	output.text = output.text[:-1]

def equals_pressed(sender):
	global clear_next
	
	expression = output.text
	clear_next = True
	
	parser = Parser()
	try:
		result.text = str(parser.parse(expression).evaluate({}))
	except Exception:
		result.text = 'What? 🧐'
	

def init():
	output.text = 'Ready! 🙂'

v = ui.load_view()
v.name = 'Calculator'

clear_next = True
output = v['output']
result = v['result']

init()

v.present('sheet')



