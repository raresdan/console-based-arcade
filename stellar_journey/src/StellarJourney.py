from stellar_journey.src.board.board import Board
from stellar_journey.src.ui.ui import Ui

class StellarJourney:
    def run(self):
        board = Board()
        ui = Ui(board)
        ui.gameplay()

