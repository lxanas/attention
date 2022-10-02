topScorers = {"Wenjia": 99, "Joyce": 96, "Wing Yan": 97}
name = input("enter the name of student, then their score will be displayed: ")
print(topScorers[name])

print("the score of the 3 students:")
for i in topScorers.items():
    print(i)

print("the average score")
sum = 0
for i in topScorers.values():
    sum += i
print(round(sum / 3))

print("the highest score")
high = 0
for i in topScorers.values():
    if high < i:
        high = i
print(high)
