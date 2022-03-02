i=0
divisors=0
number=int(input("Enter a number: "))
while i<10:
    divisors+=1
    if number==divisors:
        print(number,"is a prime number")
        break
    if number%divisors==0:
        if divisors==1:
            continue
        if number%divisors==0:
            print(number,"is not a prime number")
        break
    i-=1