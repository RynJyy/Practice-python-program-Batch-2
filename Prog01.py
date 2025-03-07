#Prog01: Create a program that ask user to input 2 numbers.
# Print the smaller number.


while True:
    try:
        Num01 = (input("\nEnter any number: "))
        Num02 = (input("Enter any number: "))
        if Num01 == Num02:
            print("\nEnter new number")
        else:
            print (f"\nThe smaller number is {min(Num01, Num02)}")
    except ValueError:
        print ("\nInvalid Input")

