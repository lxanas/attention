miles = int(input("Enter number of miles:"))
yards = int(input("Enter number of yards:"))
feet = int(input("Enter number of feet:"))
inches = int(input("Enter nuber of inches:"))
total_inches = 63360 * miles + 36 * yards + 12 * feet + inches
total_meters = total_inches / 39.37
kilometers = int(total_meters / 1000)
meters = int(total_meters - kilometers * 1000)
centimeters = (total_meters - kilometers * 1000 - meters)*100
print("Metric length:")
print(" {0:<5n} kilometers".format(kilometers))
print(" {0:<5n} meters".format(meters))
print(" {0:<5.1f} centimeters".format(centimeters))
