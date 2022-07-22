class Vaccine:
    def __init__(self,vname,loc,day) -> None:
        self.vname = vname
        self.vloc = loc
        self.vday = day

class Person(Vaccine):
        def __init__(self,name,age,deg) -> None:
            self.name = name
            self.age = age
            self.deg = deg
            
        def pushVaccine(self,vaccine,dose = None):
            self.dose = dose
            if dose == None:
                print("1st dose done for {}".format(self.name))
        def showDetail(self):
            print()
            pass


 








astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")
