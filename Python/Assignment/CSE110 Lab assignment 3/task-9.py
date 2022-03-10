string=input("Enter string: ")
char=input("Enter divider: ")
inc=0
exc=0
n=1

for count in range(len(string)):
    exc+=1
    value=ord(string[inc:exc:])
    if value!=ord(char):
        print(string[inc:exc:],end="")
    else:
        print()
    inc+=1
    
    #anothr way
#     i=input("str: ")
# j=input("spl: ")
# for item in i:
#     if item==j:
#         print()
#     else:
#         print(item,end="")    