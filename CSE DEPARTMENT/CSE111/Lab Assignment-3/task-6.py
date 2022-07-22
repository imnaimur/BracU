class Calculator:
    def __init__(self):
        print('Calculator is ready')
    def calculate(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        if self.c == '+':
            self.sum = a + b
        elif self.c == '-':
            self.sum = a - b
        elif self.c == "*":
            self.sum = a * b
        else:
            self.sum = a / b
        return self.sum
    def showCalculation(self):
       print(f"{self.a} {self.c} {self.b} = {self.sum}")
c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()