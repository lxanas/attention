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