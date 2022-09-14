num = int(input("Enter a number from 1 through 20:"))
for i in range(num + 1):
    for j in range(i):
        if j == i - 1:
            print("*")
        else:
            print("*", end="")
