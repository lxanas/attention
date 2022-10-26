from WK9.pairOfDice import pairOfDice


def roll():
    first = pairOfDice()
    second = pairOfDice()
    return first.showDie() + second.showDie()


times = 100000
count = 0
for i in range(times):
    temp = roll()
    if temp == 7:
        count += 1
print(round(count / times * 100, 2), end="")
print("%")
