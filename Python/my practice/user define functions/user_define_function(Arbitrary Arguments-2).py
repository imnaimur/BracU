num1 = input("Enter number separated by commas: ")
num1 = num1.split(",")
nam = input("Enter name: ")


def info(var1, var2):
    sum1 = 0
    for i in var1:
        sum1 += int(i)
    print(sum1, var2)

info(num1, var2=nam)

try1=input("For another try type 'Y' or any key for exit: ")
if try1=="Y" or "y":
    num1 = input("Enter number separated by commas: ")
    num1 = num1.split(",")
    nam = input("Enter name: ")
    info(num1, num1)