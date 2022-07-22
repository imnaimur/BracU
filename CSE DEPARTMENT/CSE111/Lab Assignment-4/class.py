from multipledispatch import dispatch


class Calculator:
    def __init__(self):
        print('Welcome!')

    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

    @dispatch(float, float)
    def add(self, a, b):
        sum1 = a + b
        print(sum1)

    
ca1 = Calculator()
print(ca1.add(2, 2, 3))
