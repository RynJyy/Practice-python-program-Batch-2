#Prog05: Create a program that ask user to input 2 numbers.
#Print the remainder when the first number is divided by the second number.

while True:
    try:
        Num01 = float(input("\nEnter any number: "))
        Num02 = float(input("Enter any number: "))

        if Num02 == 0:
            print ("Invalid Input")
            continue
        Remainder = (Num01 % Num02)
        print (f"The remainder when {Num01} is divided by {Num02} is {Remainder}")
    except ValueError:
        print ("Invalid Input")