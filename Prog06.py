#Prog06: Create a program that ask user to input 10 numbers.
#Print the result of the first number minus all of the remaining numbers.

while True:
    try:
        num01 = int(input("\nEnter any number 1: "))
        for i in range (9):
            num = int(input(f"Enter any number {i + 2}: "))
            num01 -= num

        print (f"\nResult: {num01}")
    except ValueError:
        print ("\nInvalid Input")
