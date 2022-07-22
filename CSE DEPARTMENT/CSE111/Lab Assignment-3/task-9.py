class Programmer:
    def __init__(self,name,lan,exp) -> None:
        self.name = name
        self.language = lan
        self.exp =  exp
        print("Horray! A new programmer is born")
    def addExp(self,n):
        self.exp += n
        print(f"Updateing experience of {self.name}")
    def printDetails(self):
        print("Name:",self.name)
        print("Language:",self.language)
        print("Experience:",self.exp)

p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()