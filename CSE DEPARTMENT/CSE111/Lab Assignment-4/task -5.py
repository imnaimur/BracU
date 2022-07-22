class Student:
    def __init__(self,name,id,dept = "CSE") -> None:
        self.name = name
        self.id = id
        self.dept = dept

    def dailyEffort(self,n):
        self.n = n
    def printDetails(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Department:",self.dept)
        print("Daily Effort:",self.n)
        if self.n<=2:
            print("Suggestion: Should give more effort!")
        elif self.n <= 4:
           print("Suggestion: Keep up the good work!")
        else:
            print("Suggestion: Excellent! Now motivate others.")
    
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()