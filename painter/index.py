import generator

if __name__ =="__main__":
    cmd = generator.cli(generator.menu)
    while True:
        command = next(cmd)
        print("from main: ", command)