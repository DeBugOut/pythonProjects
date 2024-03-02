#Defining functions
def eur(x):
    return x*0.92
def jpy(x):
    return x*150.54

#Calculations
amountUSD = float(input("Amount in USD: "))

#Results
print("Amount of money in USD is", amountUSD)
print("Amount of money in EUR is", eur(amountUSD))
print("Amount of money in JPY is", jpy(amountUSD))