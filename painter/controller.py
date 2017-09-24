from drawer import *
from fs import *

figures = []

def exit(interrupted):
    interrupted=True
    close_screen()
    return interrupted

def draw():
    # for elem in figures:
    #     print(elem)
    pen, screen = init_screen()

    print('from draw(): ', pen, screen)

    for elem in figures:
        elem(pen)

def open(ftype='json'):
    tmp = {}
    if ftype == 'json':
        tmp = load_json()
        print(tmp)
    else:
        tmp = load_pickle()
        print(tmp)
    
def save():
    print('func save')

def show():
    for elem in figures:
        print(elem)