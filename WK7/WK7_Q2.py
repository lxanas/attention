infile = open("Prof. StephenLiao.txt", 'r')
temp = infile.readline()
while temp != '':
    if "Email" in temp:
        Email = infile.readline()
        print(Email)
        break
    temp = infile.readline()
infile.close()
