import generator


if __name__ =="__main__":
    cmd = generator.cli(generator.menu)
    while not generator.interrupted:
        command = next(cmd)
        # print('We are in the node named: ', command)