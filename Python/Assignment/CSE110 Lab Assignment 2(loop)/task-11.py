i=0
count=0
number=int(input("Enter a number: "))
while i<10:
    print(number%10,end=",")
    number=number//10
    if number//10==0:
        print(number%10)
        break
    i-=1