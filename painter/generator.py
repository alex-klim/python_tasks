import collections as cl
from fs import *


def cli(submenu):
    while True:
        isLeaf = False
        print(submenu['prompt'])

        for item in submenu.items():
            if item[0] == 'func':

                item[1]()
                submenu = menu
                isLeaf = True
        
        if isLeaf == False:
            cmd = input()
            for i, item in enumerate(submenu['siblings']):
                if item['name'] == cmd:
                    submenu =  item

        yield submenu['name']
        
def draw_circle():
    pass

def draw_rectangle():
    pass

def draw():
    pass

def exit():
    print("shutting down")

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

siblings = cl.namedtuple('siblings', ['subs'])

menu = {
    'name' : 'root',
    'prompt' : 'Choose your destiny',
    'siblings' : [
            {   
                'name' : 'open',
                'prompt' : 'enter filename',
                'func' : open,
                'epilogue' : 'file opened'
            },
            {
                'name' : 'save',
                'prompt' : 'enter filename',
                'func' : save,
                'epilogue' : 'file saved'
            },
            {
                'name' : 'add',
                'prompt' : 'which figure you wanna add?(circle, rectangle)',
                'siblings' : [
                    {
                    'name' : 'circle',
                    'prompt' : 'enter x, y, radius',
                    'func' : draw_circle,
                    'epilogue' : 'circle added to image'
                    },
                    {
                    'name' : 'rectangle',
                    'prompt' : 'enter x, y, side1, side2',
                    'func' : draw_rectangle,
                    'epilogue' : 'circle added to image'
                    }
                ]
                },
            {
                'name' : 'draw',
                'prompt' : 'start drawing',
                'func' : draw
            },
            {
                'name' : 'exit',
                'prompt' : 'bye!',
                'func' : exit
            }
    ]
}