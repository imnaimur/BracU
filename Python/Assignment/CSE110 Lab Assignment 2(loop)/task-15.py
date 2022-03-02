i=0
perfect_number=0
sum=0
divisors=0 #divisors will indicate the divisor
number=int(input("Enter a number: "))
while i<10:
    divisors+=1
    if divisors==number:
        if sum==number:
            print(number,"is a perfect number")
        else :
            print(number,"is not a perfect number.")
        break
    if number%divisors==0:
        sum+=divisors
    i-=1