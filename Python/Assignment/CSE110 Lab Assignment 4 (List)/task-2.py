list1=[]
n=int(input("Enter input number: "))   
for count in range(n):
    list1+=[int(input("Enter element: "))]
if n<=3:
    print("Not possible")
else:
    print(list1[2:len(list1)-2:])
