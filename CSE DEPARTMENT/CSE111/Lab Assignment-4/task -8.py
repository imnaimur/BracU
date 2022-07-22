
class ParcelKoro:
    def __init__(self,customer = 'No name set',weight = 0) -> None:
        self.customer = customer
        self.product_weight = weight
    def calculateFee(self,location = 50):
        if location != 50:
            location = 100
        if self.product_weight == 0:
            self.total_fee = 0
        else:
            self.total_fee = (self.product_weight*20)+ location
    def printDetails(self):
        print("Customer Name:",self.customer)
        print("Product Weight:",self.product_weight)
        print("Total fee:",self.total_fee)


print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()