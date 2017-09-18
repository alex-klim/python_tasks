import collections as cl


def cli(dict_or_func):
    while True:
        print(type(dict_or_func))

        cmd = input("input one of these %s: "
        % ','.join(dict_or_func))

        print("cmd is: ", cmd)

        if(isinstance(dict_or_func[cmd], dict)):
            next(cli(dict_or_func[cmd]))
        else:
            yield cmd
        
def exit():
    print("shutting down")
    
def enter_filename():
    print("i'm entering filename")

siblings = cl.namedtuple('siblings', ['subs'])

commands = {
    'open' : {'siblings': siblings(subs=('enter_filename')),
    'enter_filename': enter_filename},
    'draw' : {},
    'exit' : exit,
}