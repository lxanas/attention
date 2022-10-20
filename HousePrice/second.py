first_data = open("cadata.csv", 'r')
first_data = [x.rstrip() for x in first_data]
first_data[0] = first_data[0] + ',ocean_proximity'
append_data = open("ocean_proximity.csv", 'r')
append_data = [x.rstrip() for x in append_data]
print(append_data[:3])

for i in range(1, len(first_data)):
    first_data[i] = first_data[i] + "," + append_data[i].split(',')[1]
    first_data[i] = first_data[i].replace(" ",'')

print(first_data[:3])

new_file = open("data_for_analysis.csv", 'w')

for x in first_data:
    new_file.writelines(x + '\n')

new_file.close()
