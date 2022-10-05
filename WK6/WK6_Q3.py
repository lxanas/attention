def getKgWeight(pounds):
    kilograms = pounds * 0.453592
    return round(kilograms, 2)


def getMHeight(feet, inches):
    heightInches = feet * 12 + inches
    meters = heightInches * 0.0254
    return round(meters, 2)


def getBMI(kilograms, meters):
    bmi = kilograms / (meters ** 2)
    return round(bmi, 2)


def BMIcategory(bmi):
    if bmi < 18.3:
        print("You are underweight")
    elif bmi < 25:
        print("You are normal weight")
    elif bmi < 30:
        print("You are overweight")
    else:
        print("You should see a doctor")


if __name__ == '__main__':
    pounds = float(input("Enter your weight in pounds: "))
    feet = int(input("Enter your height in feet: "))
    inches = float(input("Enter your height in inches: "))
    kilograms = getKgWeight(pounds)
    meters = getMHeight(feet, inches)
    bmi = getBMI(kilograms, meters)
    BMIcategory(bmi)
