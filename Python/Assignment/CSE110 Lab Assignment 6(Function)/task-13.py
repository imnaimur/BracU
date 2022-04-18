def calc():
    # global operand
    # operand=input("if you want to change the operand: ")
    sum1=0
    if operand=="+":
        sum1=num1+num2
    elif operand == "-":
        sum1=num1-num2
    elif operand == "*":
        sum1=num1*num2
    else:
        suum1=num1/num2
    return sum1
operand=input("Enter operand: ")
num1=float(input("Enter 1st number: "))
num2=float(input("Enter 2nd number: "))
print(calc())