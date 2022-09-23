infile = open("faculty.txt", 'r')
temp = list(n.rstrip() for n in infile)
print(temp[-1])
email_list = []
for i in temp:
    if i[0:5] == "Email":
        email_list.append(i)
print(email_list)
infile.close()
