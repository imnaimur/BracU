class Account:
    def __init__(self,name = "Default Account",balance = 0) -> None:
        self.balance = balance
        self.name = name

    def details(self):
        print(self.name)
        print(self.balance,end = "")
        return ""
    def withdraw(self,n):
        if n >= self.balance:
            print("Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.")
        else:
            print("Withdraw successful! New balance is: ", self.balance - n)

a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)