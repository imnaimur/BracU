class Student:
    def __init__(self,name,id,dept,cg) -> None:
        self.name = name
        self.id = id
        self.dept = dept
        self.cg = cg
        print(f"Name:{name},ID: {id}")
        print("Department:",dept)
    def calculate_CGPA(self):
        self.count = 0
        self.sum_of_ind = 0
        for i in self.cg:
            self.sum_of_ind += i * 3
            self.count +=1
        cgpa = self.sum_of_ind / (self.count*3)
        print(cgpa)
        if cgpa > 3.80:
            print("Your academic standing is 'Highest Distinction'")
        elif cgpa > 3.65:
            print("Your academic standing is 'High Distinction'")
        elif cgpa > 3.50:
            print("Your academic standing is 'Distinction'")
        elif cgpa > 2:
             print("Your academic standing is 'Satisfactory'")
        else:
             print("Your academic standing is 'Can’t Graduate'")
    def print_details(self):
        pass
s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
s1.calculate_CGPA()
print("==========================")
s1.print_details()
print("==========================")
s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
s2.calculate_CGPA()
print("==========================")
s2.print_details()
print("==========================")
s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
s3.calculate_CGPA()
print("==========================")
s3.print_details()