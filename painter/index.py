from controller import Controller
from menu import menu


if __name__ =="__main__":
    ctrl = Controller(menu)
    cmd = ctrl.cli(ctrl.menu)
    while not ctrl.interrupted:
        command = next(cmd)