# class Test:
#     def __init__(self):
#         self.sum = 0
#         self.y = 0

#     def methodA(self):
#         x=0
#         y =0
#         y = y + 7
#         x = y + 11
#         self.sum = x + y
#         print(x , y, self.sum)

#     def methodB(self):
#         x = 0
#         self.y = self.y + 11
#         x = x + 33 + self.y
#         self.sum = self.sum + x + self.y
#         print(x , self.y, self.sum)

# t1 = Test()
# t1.methodA()
# t1.methodA()
# t1.methodB()
# t1.methodB()

# class Scope:
#     def __init__(self):
#         self.x, self.y = 1, 100
#     def met1(self):
#         x = 3
#         x = self.x + 1
#         self.y = self.y + self.x + 1
#         x = self.y + self.met2() + self.y
#         print(x, self.y)
#     def met2(self):
#         y = 0
#         print(self.x, y)
#         self.x = self.x + y
#         self.y = self.y + 200
#         return self.x + y


# q2 = Scope()
# q2.met1()
# q2.met2()
# q2.met1()
# q2.met2()

class Test3:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x, y = 2, 3
        msg = [0]
        msg[0] = 3
        y = self.y + msg[0]
        self.methodB(msg, msg[0])
        x = self.y + msg[0]
        self.sum = x + y + msg[0]
        print(x, y, self.sum)
    def methodB(self, mg2, mg1):
        x = 0
        self.y = self.y + mg2[0]
        x = x + 33 + mg1
        self.sum = self.sum + x + self.y
        mg2[0] = self.y + mg1
        mg1 = mg1 + x + 2
        print(x, self.y, self.sum)



t3 = Test3()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA() 