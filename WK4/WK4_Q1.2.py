infile = open("fruit_list.csv", 'r')
temp = list(n.rstrip().split(',') for n in infile)
del temp[0]
for index in range(len(temp)):
    if temp[index][0].find("grape") != -1:
        print(temp[index])
for index in range(len(temp)):
    if float(temp[index][1]) > 50:
        print(temp[index])
infile.close()
