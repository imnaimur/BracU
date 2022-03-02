i=0
single_number=0
count=0
number=int(input("Enter a number: "))
num=number
while i<10:
    count+=1
    number//=10
    if number==0:
        break
    i-=1
i=10**(count-1)
while i>=1:
    single_number=num//i
    num%=i
    if i==1:
        print(single_number)
    else:
        print(single_number,end=",")
    i//=10