#Prog07: Create a program that ask user to input 10 numbers.
# Print how many are even numbers.

while True:
    even = 0
    try:
        for i in range (10):
            num = int(input(f"\nEnter any number {i+1}: "))
            if num % 2 == 0:
                even += 1
    except ValueError:
        print("invalid input")
    print (f"\nThe number of even in the the 10 numbers is: {even}")


