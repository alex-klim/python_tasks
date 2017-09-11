import math
import turtle

help='draw_triangle(turtle, startx, starty, a, b, c, color, fillcolor)'

def turtle_init():
	turtl = turtle.Turtle()
	turtl.up()
	return turtl

def calculate_angle(a,b,c):
	cos = (a*a+b*b-c*c)/(2*a*b)
	if(cos<-1 or cos>1):
		print("some shit went wrong")
		return -1
	angle = math.acos(cos)
	return math.degrees(angle)

def draw_triangle(turtl, startx, starty, a, b, c, color, fillcolor='white'):
	turtl.color(color)
	turtl.fillcolor(fillcolor)
	turtl.begin_fill()
	angle = calculate_angle(a, b, c)
	turtl.setpos(startx,starty)
	turtl.down()
	turtl.forward(a)
	turtl.left(angle)
	turtl.forward(b)
	turtl.setpos(startx, starty)
	turtl.seth(0)
	turtl.up()
	turtl.end_fill()
	return

trt = turtle_init()
