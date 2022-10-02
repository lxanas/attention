topScorers = {"Wenjia": {"BISA": 99}, "Joyce": {"BISB": 96}, "Wingyan": {"BDA": 97}}

print("the score of three students")
for i in topScorers.items():
    print(i[0] + ':', end="")
    print(list(i[1].values())[0])

print("the average score")
sum = 0
for i in topScorers.items():
    sum += list(i[1].values())[0]
print(round(sum / 3))

print("the highest score")
high = 0
for i in topScorers.items():
    if high < list(i[1].values())[0]:
        high = list(i[1].values())[0]
print(high)
