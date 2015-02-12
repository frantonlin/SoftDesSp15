""" Turtle World Demo """
from swampy.TurtleWorld import *

step_size = 1

def draw_pattern(turtle):
	turtle.fd(step_size)
	turtle.lt(45)
	turtle.fd(step_size)
	turtle.rt(90)
	turtle.fd(step_size)
	turtle.lt(45)
	turtle.fd(step_size)

def draw_fractal(turtle, layer):
	if layer == 1:
		draw_pattern(turtle)
	else:
		draw_fractal(turtle, layer - 1)
		turtle.lt(45)
		draw_fractal(turtle, layer - 1)
		turtle.rt(90)
		draw_fractal(turtle, layer - 1)
		turtle.lt(45)
		draw_fractal(turtle, layer - 1)



world = TurtleWorld()
beth = Turtle()
beth.undraw()
beth.x = -200
beth.y = -500
beth.draw()
beth.set_pen_color('red')
beth.set_delay(0.001)
draw_fractal(beth, 3)
wait_for_user()