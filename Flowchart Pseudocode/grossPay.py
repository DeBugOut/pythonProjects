#Define the function:
def tPay(x,y):
    return x*y

#Ask for the inputs:
hourlyRate = float(input("What is the hourly rate? \n"))
hoursWorked = float(input("What is the amount of hours worked?\n"))

#print the result:
print("The gross pay is",tPay(hourlyRate,hoursWorked))