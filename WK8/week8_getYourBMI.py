from WK8.BMI.week8_calculateBMI import getBMI, BMIcategory
from WK8.BMI.week8_getBodyInfo import getKgWeight, getMHeight

kilograms = getKgWeight()
meters = getMHeight()
bmi = getBMI(kilograms, meters)
BMIcategory(bmi)
