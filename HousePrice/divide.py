import random

train = open('train.csv', 'w')
test = open('test.csv', 'w')

raw = open('data_for_analysis.csv', 'r')
raw = [i.rstrip() for i in raw]
# print(raw[:5])
raw = raw[1:]
head = "block group ID,median house value,median income,housing median age,total rooms,total bedrooms,population,households,latitude,longitude\n"
train.write(head)
test.write(head)
for i in raw:
    num = random.random()
    if num < 0.8:
        train.write(i + '\n')
    else:
        test.write(i + '\n')
