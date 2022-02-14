#Write the Python code of a program that reads an integer, 
# and prints the integer if it is a multiple of 2 AND 5 and prints "Not multiple of 2 and 5 both" otherwise
num=int(input("Enter a number: "))
if num%2==0 and num%5==0 :
    print(num)
else :
    print("Not multiple of 2 and 5 both")