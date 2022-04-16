def unique_number(tup):
    new_number1=0
    new_number2=1
    final_number=""
    for i in(tup):
        if int(i)%2==0:
           new_number1+=int(i)
        else:
            new_number2*=int(i)
    new_number1=str(new_number1)
    new_number2=str(new_number2)
    for i in range(0,len(new_number1),2):
        final_number+=new_number1[i]
    for i in range(1,len(new_number2),2):
        final_number+=new_number2[i]
    return final_number
s="12,55,66,98,75,45,88,128"
s=s.split(",")
s=tuple(s)
print(unique_number(s))