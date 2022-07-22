
class Student:
    def __init__(self,name = "Default"):
        self.name = name
        # if self.name == None:
        #     self.name = "Default"
    def quizcalc(self,*arg):
        self.avg = 0
        count = 0
        for i in arg:
            self.avg += i
            count += 1
        self.avg = self.avg / count
    def printdetail(self):
        print(f"Hello {self.name} student")
        print(f"Your average quiz score is {self.avg}")


s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()