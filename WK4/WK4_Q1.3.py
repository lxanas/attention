infile = open("runners.txt", 'r')
temp = list(n.rstrip() for n in infile)
print(temp)
for i in temp:
    if i == '':
        temp.remove('')
print(temp)
temp.sort()
print(temp)
new = open("new.txt",'w')
for x in temp:
    new.write(x+"\n")
infile.close()
new.close()