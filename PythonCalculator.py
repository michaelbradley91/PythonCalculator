import ui
from py_expression_eval import Parser


def button_pressed(button: str):
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

def equals_pressed(sender):
	parser = Parser()
	result.text = str(parser.parse(output.text).evaluate({}))
	output.text = ''

def init():
	output.text = ''

v = ui.load_view()

output = v['output']
result = v['result']

init()

v.present('sheet')



