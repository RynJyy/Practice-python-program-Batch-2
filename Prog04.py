#Prog04: Create a program that ask user to input 2 numbers.
# Print the quotient of the two numbers without the decimal point.

while True:
    try:
        Number01 = float(input("\nEnter any number: "))
        Number02 = float(input("Enter any number: "))

        Sum = (Number01 // Number02)
        print (f"\n{Number01} / {Number02} = {Sum}")
        continue
    except ValueError:
        print("invalid input")
        continue