import turtle
import random
import math

def triangle_height(length):
    height = math.sqrt((length ** 2) - ((length/2) ** 2))
    print(height)
    if(height > 0):
        return height

def iter_sierpinski(length,depth):
    if depth==0:
        for i in range(0,3):
            trtl.forward(length)
            trtl.left(120)
    else:
        iter_sierpinski(length/2,depth-1)
        trtl.forward(length/2)
        iter_sierpinski(length/2,depth-1)
        trtl.back(length/2)
        trtl.left(60)
        trtl.forward(length/2)
        trtl.right(60)
        iter_sierpinski(length/2,depth-1)
        trtl.left(60)
        trtl.back(length/2)
        trtl.right(60)

def chaos_sierpinski(length, points):
    x1, y1 = 0, 0
    x2, y2 = length/2, triangle_height(length)
    x3, y3 = length, 0
    x, y = 0, 0
    vertices = ((x1, y1), (x2, y2), (x3, y3))

    print('x1,y1: ', x1, y1)
    print('x2,y2: ', x2, y2)
    print('x3,y3: ', x3, y3)

    for i in range(points):
        trtl.penup()
        rand_vertex = vertices[random.randint(0, 2)]
        x = (x + rand_vertex[0]) / 2
        y = (y + rand_vertex[1]) / 2
        trtl.goto(x, y)
        trtl.pendown()
        trtl.circle(1)

def sierpinski(length, mode='iter', depth=3, points=1000):
    if(length <= 0):
        return
    if(mode == 'iter'):
        iter_sierpinski(length, depth)
    elif(mode == 'chaos'):
        chaos_sierpinski(length, points)

if __name__ == "__main__":
	window = turtle.Screen()
	trtl =	turtle.Turtle()
	trtl.speed(0)
	sierpinski(200, 'iter', 4, 1000)
	window.exitonclick()
