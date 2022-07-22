class Test:
    def __init__(self,a) -> None:
        self.x1 = a
    def __init__(self,b,c) -> None:
        self.x1 = b
        self.x2 = c
    def show(self):
        print(self.x1+self.x2)

c1 = Test(2,3)
c1.show()