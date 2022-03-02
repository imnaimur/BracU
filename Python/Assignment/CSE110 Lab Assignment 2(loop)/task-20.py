sum=1
number=int(input("Enter a number: "))
for count in range (number):
    for count in range(sum):
        print(count+1,end="")
        if count+1==sum:
            print("")
            
    sum+=1