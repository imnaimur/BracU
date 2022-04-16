def find_max_min(var):
    max_number=int(var[0])
    min_number=int(var[0])
    for i in var:
        if int(i)>max_number:
            max_number=int(i)
        if int(i)<min_number:
            min_number=int(i)

    return max_number,min_number
list1=input("Enter a list: ")
list1=list1.strip("[")
list1=list1.strip("]")
list1=list1.split(",")
storage=find_max_min(list1)
a,b=storage
print("returned value from find_max_min() is:",storage)
print("Number with maximum value is: ",a)
print("Number with minimum value is: ",b)
