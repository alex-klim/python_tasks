import math
from random import randint, uniform


def sin(x, y):
    return math.sin(x), math.sin(y)

def spherical(x,y):
    return x/(x**2+y**2), y/(x**2+y**2)

def polar(x,y):
    return math.atan(y/x)/math.pi, math.sqrt(x**2+y**2)-1

def heart(x,y):
    return (math.sqrt(x**2+y**2) * math.sin(math.sqrt(x**2+y**2) * math.atan(y/x)),
           -math.sqrt(x**2+y**2) * math.cos(math.sqrt(x**2+y**2) * math.atan(y/x)))

def disk(x,y):
    return ((1/math.pi) * math.atan(y/x) * math.sin(math.pi*math.sqrt(x**2+y**2)),
            (1/math.pi) * math.atan(y/x) * math.cos(math.pi*math.sqrt(x**2+y**2)))

def fake(x,y):
    return x,y

non_linears = [sin, spherical, polar, heart, disk, fake]

def gen_coeffs():
    return [
        uniform(-1,1),
        uniform(-1,1),
        uniform(-1,1),
        uniform(-1,1),
        uniform(-2.5,2.5),
        uniform(-2.5,2.5),
        (randint(0, 255),randint(0, 255),randint(0, 255))
    ]