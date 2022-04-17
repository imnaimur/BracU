def fibonacci(num):
    num1=0
    num2=1
    sum=0
    print(num1,num2,end=" ")
    while sum<num:
        sum=num1+num2
        if sum>num:
            break
        num1=num2
        num2=sum
        print(sum,end=" ")
limit=int(input("Enter the limit: "))
fibonacci(limit)