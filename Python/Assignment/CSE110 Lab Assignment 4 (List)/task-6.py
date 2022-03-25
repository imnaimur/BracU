list1=input("enter element: ")
list1=list1.split()
max=int(list1[0])
for i in range(1,len(list1)):
  if int(list1[i])>max:
    max=int(list1[i])
    count=list1.index(str(max))
print(f"Largest number in the list is {max} which was found at index {count}.")