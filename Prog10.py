#Prog10: Create a program that ask user to input 2 numbers.
# Print all the numbers between the two numbers. Ask for two numbers from the user
while True:
    try:
        num01 = int(input("\nEnter any number: "))
        num02 = int(input("Enter any number: "))
        if num01 > num02:
            num01, num02 = num02, num01
        print(f"\nNumbers between {num01} and {num02} are:")
        for i in range(num01 + 1, num02):
            print(i, end=" ")
        if num01 + 1 == num02:
            print("\nNo numbers in between.")
        elif num01 == num02:
            print ("\nNo numbers in between.")
    except ValueError:
        print("Invalid Input")

