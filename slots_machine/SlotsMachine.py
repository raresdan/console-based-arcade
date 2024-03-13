from slots_machine.src.ui.ui import Ui


class SlotsMachine:
    def run(self):
        print("Press 'Enter' to start the game!")
        initial_balance = 20
        ui = Ui(initial_balance)
        ui.play()

