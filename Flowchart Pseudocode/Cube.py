#Defining the functions
def sideArea(x):
    return x*x
def cubeSA(x):
    return 6*x*x
def cubeVol(x):
    return x*x*x

def main():
    try:
        #Ask the user for what they want to calculate:
        choice = input("""What would you like to calculate
        1) Side Area
        2) Total Cube Side Area
        3) Cube Volume\n""")

        #Takes the value of Side Length
        sideLength = float(input("What is the side length? \n"))

        #Does each operation
        if choice == '1':
            print("The side area is",sideArea(sideLength))
        elif choice == '2':
            print("The total side area is",cubeSA(sideLength))
        elif choice == '3':
            print("The volume of the cube is",cubeVol(sideLength))

    except ValueError:
        print("Please Enter a Valid Value")

main()