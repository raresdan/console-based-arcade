from hangman.src.controller.controller import Controller
from hangman.src.repository.text_file_repository import TextFileRepository
from hangman.src.ui.ui import Ui

class Hangman:
    def run(self):
        repository = TextFileRepository()
        controller = Controller(repository)
        ui = Ui(controller)
        ui.run_app()
