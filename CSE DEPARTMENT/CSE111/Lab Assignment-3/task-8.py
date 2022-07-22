class Shinobi:
    def __init__(self,name,rank) -> None:
        self.name = name
        self.rank = rank
        self.n = 0
        self.sal = 0
    def changeRank(self,r):
        self.rank = r
    def calSalary(self,n):
        self.n = n
        if self.rank == 'Genin':
            self.sal = n * 50
        elif self.rank == 'Chunin':
            self.sal = n * 100
        else:
            self.sal = n*500
    def printInfo(self):
        print("name:",self.name)
        print("rank:",self.rank)
        print("Number of mission:",self.n)
        print("Salary:",self.sal)

naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()