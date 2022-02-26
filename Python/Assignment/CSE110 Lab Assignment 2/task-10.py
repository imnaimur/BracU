sum=0
var=0
sum1=0
sum2=0
sum3=0
sum4=0
for count in range(5):
    number=int(input("Enter a number: "))
    sum+=number
    var+=1
    if var==1:
        sum1=number
    if var==2:
        sum2=sum1+number
    if var==3:
        sum3=sum2+number
    if var==4:
        sum4=sum3+number
print(sum1)
print(sum2)
print(sum3)
print(sum4)
print(sum)