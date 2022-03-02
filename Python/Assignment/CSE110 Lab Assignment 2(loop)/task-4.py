sum=0
for count in range(600+1):
    if count%7==0 or count%9==0:
        sum+=count
print(sum)