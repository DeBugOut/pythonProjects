def timesten(x):
    return x * 10

try:
    inputValue = float(input("What number would you like to multiply by 10? \n"))
    print("The result is", round(timesten(inputValue),3))
except ValueError:
    print("Error: This is invalid please enter a valid number.")
