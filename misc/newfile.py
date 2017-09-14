import generator

if __name__ =="__main__":
    cmd = generator.cli(generator.commands)
    while True:
        command = next(cmd)
        print("from main: ", command)