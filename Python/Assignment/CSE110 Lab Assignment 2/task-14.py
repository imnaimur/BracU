i=0
loop=0 #loop will tell me how many times the loop was runned
divisors=0 #divisors will indicate the divisor
number=int(input("Enter a number: "))
while i<10:
    divisors+=1
    if divisors==number:
        loop+=1
        print(divisors)
        break
    if number%divisors==0:
        loop+=1
        print(divisors,end=",")
    i-=1
print(f"Tota {loop} divisors")