class Person:
  def __init__(self, firstname, lname,age):
    self.firstname = firstname
    self.lastname = lname
    self.age = age

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname,age):
    Person.__init__(self, firstname, lname,age)
    print(self.firstname)
 
C =Person("bob","mac",20)