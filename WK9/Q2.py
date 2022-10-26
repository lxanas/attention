from WK9.pairOfDice import pairOfDice


class Player(pairOfDice):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def showPlayer(self):
        return self.name

    def showDetail(self):
        return self.showPlayer() + ": " + str(self.showDie())


one = Player("Player 1")
two = Player("Player 2")
print(one.showDetail())
print(two.showDetail())
if one.showDie() > two.showDie():
    print(one.showPlayer() + " wins")
elif one.showDie() == two.showDie():
    print("TIE")
else:
    print(two.showPlayer() + " wins")
