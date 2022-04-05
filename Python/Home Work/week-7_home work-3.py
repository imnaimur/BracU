string=input("Enter Number: ")
string=string.split(",")
string1=[]
magic_number=[]
non_magic_number=[]
# for i in string:
#     string1.append(int(i))
# 442310,441310,42251,42241,451,452
for i in string:
    sum1=0
    sum2=0
    for j in range(len(i)):
        if j%2==0:
            sum1+=int(i[j])
        else:
            sum2+=int(i[j])
    if(sum1==sum2):
        magic_number.append(int(i))
    else:
        non_magic_number.append(int(i))
magic_number=tuple(magic_number)
non_magic_number=tuple(non_magic_number)
print(f"({magic_number},{non_magic_number})")