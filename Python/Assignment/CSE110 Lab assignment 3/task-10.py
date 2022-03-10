i=(input("enter a string: "))
ind=0
for x in i:
    if x not in i[ind-1]:
        print(x)
    ind+=1