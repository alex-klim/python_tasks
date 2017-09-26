from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    
    @abstractmethod
    def __init__():
        pass
    
    @abstractmethod
    def draw():
        pass

class Circle(Shape):

    def __init__(self, data=None):
        if data == None:
            self.coordinates, self.radius, self.color = self.get_parameters()
            self.name = __class__.__name__
        else:
            self.name = data['name']
            self.coordinates = data['coordinates']
            self.radius = data['radius']
            self.color = data['color']

    def __repr__(self):
        return 'Circle(coordinates: {}, radius: {}, color: {})'.format(self.coordinates, self.radius, self.color)
    
    def get_parameters(self):
        while True:
            args = input('enter x, y, radius\n')
            color = input('choose color:\n')
            *coordinates, radius = (int(arg) for arg in args.split(' '))
            if radius <= 0:
                print('incorrect arguments\n')
            else:
                return (coordinates, radius, color)
            print('try again:\n')

    def draw(self, pen):
        pen.color(self.color)
        pen.up()
        pen.goto(self.coordinates[0],self.coordinates[1]-self.radius)
        pen.down()
        pen.circle(self.radius)
        pen.up()
        pen.home()

class Rectangle(Shape):

    def __init__(self, data=None):
        if data == None:
            self.coordinates, self.side1, self.side2, self.color = self.get_parameters()
            self.name = __class__.__name__
        else:
            self.name = data['name']
            self.coordinates = data['coordinates']
            self.side1 = data['side1']
            self.side2 = data['side2']
            self.color = data['color']

    def __repr__(self):
        return 'Rectangle(coordinates: {}, side1: {}, side2: {}, color: {})'.format(self.coordinates, self.side1, self.side2, self.color)

    def get_parameters(self):
        while True:
            args = input('enter x, y, side1, side2\n')
            color = input('choose color:\n')
            *coordinates, side1, side2 = (int(arg) for arg in args.split(' '))
            if side1 <= 0 or side2 <= 0:
                print('incorrect arguments\n')
            else:
                return (coordinates, side1, side2, color)
            print('try again:\n')

    def draw(self, pen):
        pen.color(self.color)
        pen.up()
        pen.goto(self.coordinates[0],self.coordinates[1])
        pen.down()
        pen.forward(self.side1)
        pen.left(90)
        pen.forward(self.side2)
        pen.left(90)
        pen.forward(self.side1)
        pen.left(90)
        pen.forward(self.side2)
        pen.left(90)
        pen.up()
        pen.home()
