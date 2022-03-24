list1=[]
list2=[]
# n1=int(input("length of 1st list: "))
# for i in range(n1):
#   val1=int(input("element: "))
#   list1.append(val1)
# n2=int(input("length of 2nd list: "))
# for j in range(n2):
#   val2=int(input("element: "))
#   list2.append(val2)
# print(list1[:-1]+list2)
sr1=input("enter 1st list element: ")
sr1=sr1.split()
sr2=input("enter 2nd list element: ")
sr2=sr2.split()
for i in range(len(sr1)):
    list1.append(int(sr1[i]))
for j in range(len(sr2)):
    list2.append(int(sr2[j]))
print(list1[:-1]+list2)