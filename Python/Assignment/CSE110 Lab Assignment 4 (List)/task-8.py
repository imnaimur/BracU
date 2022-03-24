# split function convert string into list
list1=[]
sr1=input("enter 1st list element: ")
sr1=sr1.split(" ")
sr2=input("enter 2nd list element: ")
sr2=sr2.split(" ")
for i in range(len(sr1)):
    if int(sr1[i])%2==0:
        list1.append(int(sr1[i]))
for j in range(len(sr2)):
    if int(sr2[j])%2==0:
        list1.append(int(sr2[j]))
print(list1)