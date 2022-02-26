sum=0
total=0
for count in range(10):
    num=int(input("Enter a number: "))
    if num%2!=0:
        sum+=num
        total+=1
print("The total of the odd numbers is ",sum,end=" ") 
print("and the average is ",sum/total)