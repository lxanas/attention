ID = input("Enter your name and student ID: ")
SPY = float(input("Enter the amount invested in SPY: "))
QQQ = float(input("Enter the amount invested in QQQ: "))
EEM = float(input("Enter the amount invested in EEM: "))
GGG = float(input("Enter the amount invested in GGG: "))
count = SPY + QQQ + EEM + GGG
shareS = SPY / count
shareQ = QQQ / count
shareE = EEM / count
shareG = GGG / count
print("{0:<6s}{1:<6.2%}".format("SPY", shareS))
print("{0:<6s}{1:<6.2%}".format("QQQ", shareQ))
print("{0:<6s}{1:<6.2%}".format("EEM", shareE))
print("{0:<6s}{1:<6.2%}".format("GGG", shareG))
print("TOTAL AMOUNT INVESTED for {0:s}: ${1:10,.2f}.".format(ID, count))
