#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

odd = 0
i = 0
while i <= 100:
    if i % 2 != 0:
        print (f"{i} is odd number")
        odd += 1
    i += 1
print (f"\nThe total odd numbers out of 100 is {odd}")
