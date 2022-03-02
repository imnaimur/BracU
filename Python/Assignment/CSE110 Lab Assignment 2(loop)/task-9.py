n=int(input("Enter a number: "))
sum=0
for count in range(n+1):
    if count%7==0:
        sum+=count
print(sum)