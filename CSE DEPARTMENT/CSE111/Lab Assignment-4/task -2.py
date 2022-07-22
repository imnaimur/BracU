class Panda:
    def __init__(self,name,gnd,age):
        self.name = name
        self.gender = gnd
        self.age = age
    def sleep(self,arg = None):
        if arg == None:
            print(f"{self.name}'s duration is unknown thus should have only bamboo leaves", end = '')
        else:
            print(f"{self.name} sleeps {arg} hours daily and should have Broccoli Chicken", end = '')
        return ""
panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())