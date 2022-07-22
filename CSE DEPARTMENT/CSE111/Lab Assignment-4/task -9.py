class Batsman:
    def __init__(self,*arg) -> None:
        if len(arg)<3:
            self.name = "New Batsman"
            self.run = arg[0]
            self.ball = arg[1]
        else:
            self.name = arg[0]
            self.run = arg[1]
            self.ball = arg[2]
    def setName(self,name):
        self.name = name
    def printCareerStatistics(self):
        print("Name:",self.name)
        print(f"Runs Scored: {self.run}, balls Faced: {self.ball}")
    def battingStrikeRate(self):
        rate = (self.run/self.ball)*100
        return rate

b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())