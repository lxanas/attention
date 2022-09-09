rate = float(input("Enter your target ANNUAL rate of return (without the % sign):"))
total = 3000 * (((1 + rate/12) ** (38 * 12) - 1) / (rate/12))
print("With a total monthly contribution of $3000, your MPF will worth ${0:.2f} after 38 years.".format(total))
print("That is about {0:.1f} million(s).".format(total/1000000))
