#Prog03: Create a program that ask user to input 2 numbers.
# Print the difference of the two numbers.

while True:
    try:
        Num01 = int(input("\nEnter any number: "))
        Num02 = int(input("Enter any number: "))

        diff = Num01 - Num02
        diff = abs(diff)
        print (f"\nThe difference of the two numbers is {diff}")
    except ValueError:
        print ("Invalid Input")