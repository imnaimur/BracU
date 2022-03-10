string=input("Enter a string: ")
inc=0    #inc for included index 
exc=0    #exc for excluded index
for count in range(len(string)):
    exc+=1
    val=ord(string[inc:exc:])
    if 90<val+1<97:
        val2=val+7
        char=chr(val2)
        print(char,end="") 
    elif 32<=val+1<=90 or 97<= val+1<=122:
        val2=val+1
        char=chr(val2)
        print(char,end="")
    else:
        val2=val-80
        char=chr(val2)
        print(char,end="")
    inc+=1
    
    # another way
# i=input()
# for x in i:
#     val=ord(x)
#     val2=val+1
#     if val2>122:
#         val2=val-90
#         print(chr(val2),end="")
#     elif 96>val2>90:
#         val2=val+7
#         print(chr(val2),end="")
#     else:
#         print(chr(val2),end="")