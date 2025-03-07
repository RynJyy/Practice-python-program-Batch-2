#Prog02: Create a program that ask user to input 2 numbers.
# Print "Not Equal" when the numbers are not the same.

while True:
    try:
        Num01 = (input("\nEnter any number: "))
        Num02 = (input("Enter any number: "))

        if Num01 < Num02 or Num01 > Num02:
            print ("\nNot Equal")
        else:
            print ("\nEnter new number")
    except ValueError:
        print ("\nInvalid Input")