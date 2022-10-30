from WK9.pairOfDice import PairOfDice

one = PairOfDice()
two = PairOfDice()
one.roll()
two.roll()
print("Player 1: " + str(one.sum()))
print("Player 2: " + str(two.sum()))
if one.sum() > two.sum():
    print("Player 1 wins")
elif one.sum() == two.sum():
    print("TIE")
else:
    print("Player 2 wins")
