bill = float(input("Enter amount of bill: "))
rate = 0.15
tip = rate * bill
if tip >= 2:
    print("Tip is ${0:.2f}".format(tip))
else:
    print("Tip is $2.00")
