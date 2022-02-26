i=0
count=0
number=int(input("Enter a number: "))
while i<10:
    count+=1
    number=number//10
    if number==0:
        break
    i-=1
print(number)