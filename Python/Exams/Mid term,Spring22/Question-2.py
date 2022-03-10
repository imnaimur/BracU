num1=input("enter  a number: ")
num2=input("enter  a number: ")
sr1=''
sr2=''
sr3=''
sr4=''
val1=0
val2=0
ind1=0
ind2=0
for x in range(len(num1)):
    val1=int(num1[ind1])
    if val1%2==0:
        sr1+=str(val1)
    else:
        sr2+=str(val1)
    ind1+=1
for x in  range(len(num2)):
    val2=int(num2[ind2])
    if val2%2==0:
        sr3+=str(val2)
    else:
        sr4=str(val2)
    ind2+=1
print("the first number: ",sr1+sr4)
print("the second number: ",sr2+sr3)