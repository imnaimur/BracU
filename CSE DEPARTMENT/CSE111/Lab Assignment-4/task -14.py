class StudentDatabase:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id
        self.grades = {}
       

    def calculateGPA(self,list1,session):
        self.list1 = []
        self.list2 = []
        self.gpa = 0
        self.session = session
        temp_dict = {}
        for i in list1:
            i = i.split(":")
            self.list1.append(i[0])
            self.list2.append(float(i[1]))
        for j in self.list2:
            self.gpa += j
        self.gpa = self.gpa/len(self.list2)
        self.gpa = "%.2f"%self.gpa
        temp_dict.update({tuple(list1):float(self.gpa)})
        self.grades.update({self.session:temp_dict})
    def printDetails(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print(f"Course taken in {self.session}:")
        for x in self.list1:
            print(x)
        print("GPA",self.gpa)

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 
'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 
'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()