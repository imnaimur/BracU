class UberEats:
    def __init__(self,name,phone,location) -> None:
        self.name = name
        self.phone = phone
        self.location = location
        print(f"{self.name} welcome to UberEats!")
    def add_items(self,itm1,itm2,pr1,pr2):
        self.item1 = itm1
        self.item2 = itm2
        self.price1 = pr1
        self.price2 = pr2
    def print_order_detail(self):
        sum = self.price1+self.price2
        dict1 = {self.item1:self.price1,self.item2:self.price2}
        print(f"User details: Name:{self.name},Phone: {self.phone},Address: {self.location}")
        print("Order: ",dict1)
        print("Total Paid Ammount: ",end = "")
        return sum

        
order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())