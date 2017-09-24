def circle_validator(func):
    def shiny_imperator(pen, x=0, y=0, r=100):
        while True:
            if r <= 0:
                print('incorrect arguments')
            else:
                return func(pen)
            arg = input('try again:\n')
    return shiny_imperator

def rectangle_validator(func):
    def shiny_imperator(pen, x=0, y=0, a=200, b=100):
        while True:
            if a <= 0 or b <= 0:
                print('incorrect arguments')
            else:
                return func(pen)
            arg = input('try again:\n')
    return shiny_imperator