import random
from time import sleep

import texttable


class Machine:
    def __init__(self):
        self.__data = [[" " for _ in range(3)] for _ in range(3)]
        self.__symbols = ["🍒", "🍉", "🍋", "🍊", "🍇", "7️⃣", "🧛"]

    def __str__(self):
        board = texttable.Texttable()
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.__data[i][j])
            board.add_row(row)
        return board.draw()

    def spin(self):
        for i in range(3):
            for j in range(3):
                self.__data[i][j] = random.choice(self.__symbols)
        print(self.__str__())

    def winSymbol(self):
        symbols = []
        # first diag
        if self.__data[0][0] == self.__data[1][1] == self.__data[2][2]:
            symbols.append(self.__data[0][0])
        # first row
        if self.__data[0][0] == self.__data[0][1] == self.__data[0][2]:
            symbols.append(self.__data[0][0])
        # second row
        if self.__data[1][0] == self.__data[1][1] == self.__data[1][2]:
            symbols.append(self.__data[1][0])
        # third row
        if self.__data[2][0] == self.__data[2][1] == self.__data[2][2]:
            symbols.append(self.__data[2][0])
        # second diagonal
        if self.__data[2][0] == self.__data[1][1] == self.__data[0][2]:
            symbols.append(self.__data[2][0])
        return symbols

    def calculatePrize(self, symbols):
        total = 0
        for symbol in symbols:
            total += self.getPrize(symbol)
        return total

    def getPrize(self, symbol):
        if symbol == "🍒":
            return 50
        if symbol == "🍉":
            return 50
        if symbol == "🍋":
            return 25
        if symbol == "🍊":
            return 25
        if symbol == "🍇":
            return 100
        if symbol == "7️⃣":
            return 250
        if symbol == "🧛":
            return self.special()
        if symbol is None:
            return 0

    def special(self):
        spins = 15
        totalPrize = 200
        while spins:
            self.spin()
            spins -= 1
            print(f"Special prize: {totalPrize}")
            sleep(1)
            symbols = self.winSymbol()
            if "🧛" in symbols:
                spins += 10
            else:
                totalPrize += self.calculatePrize(symbols)
        return totalPrize
