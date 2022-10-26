from WK9.pairOfDice import pairOfDice

red = pairOfDice()
blue = pairOfDice()
print("Red die: " + str(red.showDie()))
print("Blue die: " + str(blue.showDie()))
print("Total: " + str(red.showDie() + blue.showDie()))
