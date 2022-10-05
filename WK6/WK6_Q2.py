# Q2
infile = open("names.txt", 'r')
text = infile.read()
print(text)
infile.close()

# Q2.1
infile = open("names.txt", 'r')
text = infile.readline()
nameList = []
while text != '':
    temp = nameList.append(text.rstrip().split(';'))
    text = infile.readline()
for i in nameList:
    for j in i:
        print(j)
infile.close()

# Q2.2
infile = open("names.txt", 'r')
text = infile.readline()
nameList = []
newList = []
while text != '':
    temp = nameList.append(text.rstrip().split(';'))
    text = infile.readline()
for i in nameList:
    for j in i:
        newList.append(j)
newList.sort()
# print(newList)
infile.close()
outfile = open("new.txt", 'w')
for i in newList:
    outfile.write(i + '\n')
outfile.close()


# Q2.3
def myfunc(file):
    infile = open(file, 'r')
    text = infile.readline()
    nameList = []
    newList = []
    while text != '':
        temp = nameList.append(text.rstrip().split(';'))
        text = infile.readline()
    for i in nameList:
        for j in i:
            newList.append(j)
    newList.sort()
    infile.close()
    outfile = open("new.txt", 'w')
    for i in newList:
        outfile.write(i + '\n')
    outfile.close()


if __name__ == '__main__':
    name = input("input your file name:")
    myfunc(name)
