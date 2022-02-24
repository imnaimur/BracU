sum1=0
sum2=0
for count in range(600+1):
    if count%7==0 or count%9==0:
        sum1+=count
    if count%7==0 and count%9==0:
        sum2+=count
print(sum1-sum2)