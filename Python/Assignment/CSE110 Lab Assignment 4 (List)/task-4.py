list1=[]
list2=[]
n=int(input("length of list: "))
for count in range(n):
    val=int(input("Enter element: ")) 
    list2+=[val]
    val=val**2
    list1.append(val)
print(list2)
print(list1)