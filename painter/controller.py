import sys
from functools import wraps
from drawer import *
from fs import *


class Controller:

    def __init__(self, menu):
        self.figures = []
        self.shapes = ['circle', 'rectangle']
        self.interrupted = False
        self.drawer = Drawer()
        self.menu = menu
        self.fill_menu(menu)

    def exit(self):
        self.interrupted=True
        self.drawer.close_screen()

    def draw(self):
        self.drawer.clearscreen()
        for elem in self.figures:
            self.drawer.draw(elem)

    def open_file(self, ftype='json'):
        self.figures = []
        filename = input()
        filetype = filename.split('.')[-1]
        if filetype == 'json' or filetype == 'pickle':
            ftype = filetype
        if ftype == 'json':
            tmp = load_json(filename)
        elif ftype == 'pickle':
            tmp = load_pickle(filename)
        for i, item in enumerate(tmp):
            self.figures.append(self.dict_to_obj(item))

    def dict_to_obj(self, data):
        if data['name'] == 'Circle':
            return Circle(data)
        if data['name'] == 'Rectangle':
            return Rectangle(data)
        
    def save_file(self, ftype='json'):
        data = []
        for shape in self.figures:
            data.append(vars(shape))

        filename = input()
        filetype = filename.split('.')[-1]
        if filetype == 'json' or filetype == 'pickle':
            ftype = filetype
        if ftype == 'json':
            save_json(data, filename)
        elif ftype == 'pickle':
            save_pickle(data, filename)

    def show(self):
        for elem in self.figures:
            print(elem)
        print("")

    def fill_menu(self, submenu):
        for item in submenu.items():
            if item[0] == 'func':
                if hasattr(self, item[1]):
                    submenu[item[0]] = getattr(self, item[1])
            if item[0] == 'siblings':
                for shape in item[1]:
                    self.fill_menu(shape)

    def add_figure(self, name):
        this_module = sys.modules[__name__]
        print('(II) adding figure: {}'.format(name))
        
        if hasattr(this_module, name):
            class_name = getattr(this_module, name)
            self.figures.append(class_name())
            print('(++) figure {} added:'.format(name))
        else:
            print('net figure')

    def cli(self, submenu):
        while True:
            isLeaf = False
            print(">> {}".format(submenu['prompt']))

            for item in submenu.items():
                if item[0] == 'func':
                    if callable(item[1]):
                        if submenu['name'] in self.shapes:
                            item[1](submenu['name'].capitalize())
                        else:
                            item[1]()
                    else:
                        raise NotImplemented
                    submenu = self.menu
                    isLeaf = True
                
            if not isLeaf:
                cmd = input('$ ')
                for i, item in enumerate(submenu['siblings']):
                    if item['name'] == cmd:
                        submenu = item

            yield submenu['name']