import random

from slots_machine.src.machine.machine import Machine


class Ui:
    def __init__(self, balance):
        self.__machine = Machine()
        self.__balance = balance
        self.__stake = 1

    @staticmethod
    def double(prize):
        cards = ["♠️", "♣️", "♥️", "♦️"]
        for _ in range(4):
            chosenColor = input("Color: ")
            chosenCard = random.choice(cards)
            if chosenColor == "a" and (chosenCard == "♥️" or chosenCard == "♦️"):
                prize = prize * 2
                print(chosenCard)
            elif chosenColor == "d" and (chosenCard == "♠️" or chosenCard == "♣️"):
                prize = prize * 2
                print(chosenCard)
            elif chosenColor == "":
                break
            else:
                print(chosenCard)
                prize = 0
                break
        return prize

    def play(self):
        while True:
            while True:
                try:
                    option = input("")
                    break
                except ValueError as ve:
                    print("Invalid option", ve)
            if option == "stake":
                self.__stake = int(input("> "))
            if option == "":
                if self.__balance == 0:
                    print("No more credits!")
                    break
                if self.__balance < self.__stake:
                    print("Not enough credits!")
                    print(f"Balance: {self.__balance}")
                else:
                    self.__machine.spin()
                    self.__balance -= self.__stake
                    symbols = self.__machine.winSymbol()
                    prize = self.__machine.calculatePrize(symbols) * self.__stake
                    if symbols:
                        print(f"You won: {prize} credits!")
                        doubleInput = input("Do you wanna double?")
                        if doubleInput == "yes":
                            doublePrize = self.double(prize)
                            self.__balance += doublePrize
                            print(f"You won: {doublePrize} 💵!")
                        elif doubleInput == "no" or doubleInput == "":
                            self.__balance += prize
                    print(f"Balance: {self.__balance}💵")
            if option == "exit":
                break
