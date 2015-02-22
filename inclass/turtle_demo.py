""" Turtle World Demo """
from swampy.TurtleWorld import *

step_size = 5

def draw_koch_base(turtle):
	turtle.fd(step_size)
	turtle.lt(60)
	turtle.fd(step_size)
	turtle.rt(120)
	turtle.fd(step_size)
	turtle.lt(60)
	turtle.fd(step_size)

def draw_koch(turtle, layer):
	if layer == 1:
		draw_koch_base(turtle)
	else:
		draw_koch(turtle, layer - 1)
		turtle.lt(60)
		draw_koch(turtle, layer - 1)
		turtle.rt(120)
		draw_koch(turtle, layer - 1)
		turtle.lt(60)
		draw_koch(turtle, layer - 1)

def draw_snowflake(turtle, layers):
	draw_koch(turtle, layers)
	turtle.rt(120)
	draw_koch(turtle, layers)
	turtle.rt(120)
	draw_koch(turtle, layers)
	turtle.rt(120)

def draw_tree_base(turtle):
	turtle.fd(step_size)
	turtle.fd(step_size)
	new_turtle = Turtle()
	new_turtle.x = turtle.x
	new_turtle.y = turtle.y
	new_turtle.heading = turtle.heading
	new_turtle.rt(30)
	new_turtle.fd(step_size)
	new_turtle.fd(step_size)
	new_turtle.undraw()
	turtle.fd(step_size)
	turtle.lt(30)
	turtle.fd(step_size)
	turtle.fd(step_size)

def draw_tree(turtle, layer):
	if layer == 1:
		draw_tree_base(turtle)
	else:
		draw_tree(turtle, layer - 1)
		draw_tree(turtle, layer - 1)
		new_turtle = Turtle()
		new_turtle.x = turtle.x
		new_turtle.y = turtle.y
		new_turtle.heading = turtle.heading
		new_turtle.rt(30)
		draw_tree(new_turtle, layer - 1)
		draw_tree(new_turtle, layer - 1)
		new_turtle.undraw()
		draw_tree(turtle, layer - 1)
		turtle.lt(30)
		draw_tree(turtle, layer - 1)
		draw_tree(turtle, layer - 1)	


world = TurtleWorld()
beth = Turtle()
"""beth.undraw()
beth.x = 0
beth.y = -25
beth.draw()
beth.set_pen_color('red')
beth.set_delay(0.0000001)
draw_snowflake(beth, 6)"""
beth.undraw()
beth.x = 1000
beth.y = -500
beth.heading = 90
beth.draw()
beth.set_pen_color('red')
beth.set_delay(0.01)
draw_tree(beth, 2)
wait_for_user()