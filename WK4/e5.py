file = open("school_student.txt", 'r')
all = [x.strip().split(',') for x in file]
print(all)
for i in range(len(all)):
    temp = int(all[i][1]) / int(all[i][2])
    all[i].append(str(round(temp)))
write = open("school_student_new.txt", 'w')
sep = ","
for x in all:
    write.writelines(sep.join(x) + "\n")
write.close()
file.close()
