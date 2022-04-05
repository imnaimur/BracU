string=(input("Enter number separated by  comas: "))
string=string.strip("(")
string=string.strip(")")
string=string.split(",")
tuple1=[]
for i in string:
    tuple1.append(int(i))
tuple1=tuple(tuple1)
tuple1=tuple1[2:-2:]
print(tuple1)