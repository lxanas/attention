data = open("Absenteeism_at_work.csv", "r")
data = [line.strip() for line in data]
print(data[:5])
# for i in range(len(data)):
#     data[i] = data[i].replace(";", ',')
# print(data[:5])
# new = open("new.csv", "w")
# for line in data:
#     new.write(line + "\n")
new.close()
