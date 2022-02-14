# Task 7
# Write the Python code of a program that reads an integer, and prints the integer it is a multiple of either 2 or 5 but not both.
# If the number is a multiple of 2 and 5 both, then print "Multiple of 2 and 5 both".
# For all other numbers, the program prints "Not a multiple we want".
num=int(input("Enter a number: "))
if num%2==0 and num%5==0:
    print("Multiple of 2 and 5 both")
elif num%5==0:
    print(num)
elif  num%2==0:
    print(num)
else :
    print("Not a multiple we want")