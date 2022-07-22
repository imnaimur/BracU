class TaxiLagbe:
    def __init__(self,number_plate,area) -> None:
        self.number_plate = number_plate
        self.area = area
        self.passenger = []


    def addPassenger(self,*arg):
        # for j in range(len(arg)):
            passenger = []
            for i in arg:
                i = i.split("_")
                passenger.append(i[0])
            self.passenger.extend(passenger)
            for j in range(len(arg)):
                print(f"Dear {passenger[j]}! Welcome to Taxilagbe")
                


    def printDetails(self):
        print("Trip info for Taxi number:",self.number_plate)
        print("This taxi can cover only {} area".format(self.area))
        print("Total passengers:",len(self.passenger))
        print("Passenger lists: ")
        print(*self.passenger,sep = ",")
taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()