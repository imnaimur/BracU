
n=int(input("Enter a Number: "))
sum1=0
sum2=0
for count in range(n+1):
    if count%2!=0:
        sum1+=count**2
    if count%2==0:
        sum2+=count**2
print(sum1-sum2)