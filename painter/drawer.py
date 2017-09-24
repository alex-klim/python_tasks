import turtle
from validator import *


screen = None
pen = None

def init_screen():
    global screen, pen
    pen = pen or turtle.Turtle()
    screen = turtle.Screen()
    screen.reset()
    return pen, screen

def close_screen():
    global screen
    if screen:
        screen.bye()

@circle_validator
def draw_circle(pen, x=0, y=0, r=100):
    pen.up()
    pen.goto(x,y-r)
    pen.down()
    pen.circle(r)
    pen.up()
    pen.home()

@rectangle_validator
def draw_rectangle(pen, x=0, y=0, a=100, b=200):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.forward(a)
    pen.left(90)
    pen.forward(b)
    pen.left(90)
    pen.forward(a)
    pen.left(90)
    pen.forward(b)
    pen.left(90)
    pen.up()
    pen.home()