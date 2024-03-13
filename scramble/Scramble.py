from scramble.src.controller.controller import Controller
from scramble.src.repository.repository import Repository
from scramble.src.ui.ui import Ui

class Scramble:
    def run(self):
        repository = Repository()
        controller = Controller(repository)
        ui = Ui(controller)
        print("     WELCOME TO SCRAMBLE!")
        print()
        ui.gameplay()
