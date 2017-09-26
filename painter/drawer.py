import turtle
from shape import *

class Drawer:

    def __init__(self, pen=None, screen=None):
        if pen is None:
            self.pen = turtle.Turtle()
        else:
            self.pen = pen
        if screen is None:
            self.screen = turtle.Screen()
        else:
            self.screen = screen

    def draw(self, shape):
        try:
            shape.draw(self.pen)
        except AttributeError:
            print("Not a drawable object")

    def clearscreen(self):
        self.pen.clear()
    
    def close_screen(self):
        if self.screen:
            self.screen.bye()