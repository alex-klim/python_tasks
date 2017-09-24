from menu import *
interrupted = False

def cli(submenu):
    while True:
        global interrupted
        isLeaf = False
        print(">> {}".format(submenu['prompt']))

        for item in submenu.items():
            if item[0] == 'func':
                if item[1] == draw:
                    draw()
                elif item[1] == exit:
                    interrupted = exit(interrupted)
                elif item[1] == show:
                    show()
                else:
                    figures.append(item[1])
                submenu = menu
                isLeaf = True
        
        if not isLeaf:
            cmd = input()
            for i, item in enumerate(submenu['siblings']):
                if item['name'] == cmd:
                    submenu =  item

        yield submenu['name']