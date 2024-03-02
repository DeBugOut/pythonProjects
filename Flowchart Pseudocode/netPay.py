#Define the function:
def tPay(x,y):
    return x*y
def tax(r,g):
    return r*g 
def netPay(g,t):
    return g-t

#Ask for the inputs:
hourlyRate = float(input("What is the hourly rate? \n"))
hoursWorked = float(input("What is the amount of hours worked?\n"))
holdingTaxrate = float(input("What is the holding tax rate? (in decimals)\n"))

#Hold using a variable:
grossPay = tPay(hourlyRate,hoursWorked)
taxAmount = tax(holdingTaxrate,grossPay)

#Print the result:
print("The net pay after taxes is",netPay(grossPay,taxAmount))