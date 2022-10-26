import random


class pairOfDice:
    def __init__(self):
        self.die = random.randint(1, 6)

    def showDie(self):
        return self.die
