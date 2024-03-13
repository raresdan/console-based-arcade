from battleships.src.Battleships import Battleships
from hangman.src.Hangman import Hangman
from order_and_chaos_one.src.OrderAndChaosOne import OrderAndChaosOne
from order_and_chaos_two.src.OrderAndChaosTwo import OrderAndChaosTwo
from scramble.Scramble import Scramble
from slots_machine.SlotsMachine import SlotsMachine
from stellar_journey.src.StellarJourney import StellarJourney


def menu():
    print("1. Battleships")
    print("2. Hangman")
    print("3. Order & Chaos (1st Edition)")
    print("4. Order & Chaos (2nd Edition)")
    print("5. Scramble")
    print("6. Stellar Journey")
    print("7. Slots Machine")
    print("0. Exit")

if __name__ == "__main__":
    menu()
    while True:
            while True:
                try:
                    print()
                    option = int(input("What game do you want to play? \n"))
                    print()
                    break
                except ValueError:
                    print("Invalid command!")
            if option == 1:
                Battleships().run()
            elif option == 2:
                Hangman().run()
            elif option == 3:
                OrderAndChaosOne().run()
            elif option == 4:
                OrderAndChaosTwo().run()
            elif option == 5:
                Scramble().run()
            elif option == 6:
                StellarJourney().run()
            elif option == 7:
                SlotsMachine().run()
            elif option == 0:
                print("The menu was exited successfully!")
                break
            else:
                print("Invalid command!")
                print()