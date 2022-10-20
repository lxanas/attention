raw_data = open("cadata.txt", 'r', encoding="utf8")
raw_data = [x.rstrip() for x in raw_data]
raw_data = raw_data[27:]
# Q3.1

print(raw_data[0:2])

for i in range(len(raw_data)):
    raw_data[i] = raw_data[i].replace("\t", ",")
    raw_data[i] = raw_data[i].replace(" ", ",")

print(raw_data[0:2])

# test = raw_data[0]
# print(test)
# test = test.split(',')
# print(test)
# for i in range(len(test)):
#     test[i] = eval(test[i])
#
# print(test)

for i in range(len(raw_data)):
    temp = raw_data[i].split(',')
    for j in range(len(temp)):
        temp[j] = eval(temp[j])
    raw_data[i] = ''.join(str(temp))[1:-1]

# print(raw_data)

new_file = open("cadata.csv", 'w')

raw_data.insert(0,
                "block group ID,median house value,median income,housing median age,total rooms,total bedrooms,population,households,latitude,longitude")
for x in raw_data:
    new_file.writelines(x + '\n')

new_file.close()

# Q3.2
