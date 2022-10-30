from WK9.pairOfDice import PairOfDice

times = 100000
count = 0
for i in range(times):
    temp = PairOfDice()
    temp.roll()
    temp = temp.sum()
    if temp == 7:
        count += 1
print(round(count / times * 100, 2), end="")
print("%")
