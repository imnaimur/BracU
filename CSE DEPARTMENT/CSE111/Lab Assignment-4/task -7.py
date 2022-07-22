class Match:
    def __init__(self,team) -> None:
        team = team.split("-")
        self.batting = team[0]
        self.bowling = team[1]
        self.wicket = 0
        print("5..4..3..2..1.. Play !!!")
    def add_run(self,r):
        self.run = 0
        self.run +=r
    def add_over(self,o):
        self.over = 0
        if (self.over +=o ) >= 5:
            print("Warning! Cannot add {} over/s (5 over match)".format(o))
        else:
            self.over += o
    def add_wicket(self,w):
       
        self.wicket +=w
    def print_scoreboard(self):
        print("Batting Team:",self.batting)
        print("Bowling Team:",self.bowling)
        print(f"Total Runs: {self.run} Wicket: {self.wicket} Overs: ", end = "")
        return self.over

match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())