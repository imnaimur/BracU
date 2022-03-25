sr1=input("enter 1st list element: ")
sr1=sr1.split()
sr2=input("enter 2nd list element: ")
sr2=sr2.split()
for i in sr1:
    if i in sr2:
        print(True)
        break
    else:
        print(False)
