def getKgWeight():
    pounds = float(input("Enter your weight in pounds: "))
    kilograms = pounds * 0.453592
    return round(kilograms, 2)


def getMHeight():
    feet = int(input("Enter your height in feet: "))
    inches = float(input("Enter your height in inches: "))
    heightInches = feet * 12 + inches
    meters = heightInches * 0.0254
    return round(meters, 2)
