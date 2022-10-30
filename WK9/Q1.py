from WK9.pairOfDice import PairOfDice

a = PairOfDice()
a.roll()
print("Red die: " + str(a.getRedDie()))
print("Blue die: " + str(a.getBlueDie()))
print("Total: " + str(a.sum()))

