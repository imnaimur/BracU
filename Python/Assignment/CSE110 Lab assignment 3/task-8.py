string=input("Enter a string: ")
exc=0
inc=0
for count in range(len(string)):
    exc+=1
    if inc%2!=0:
        val=ord(string[inc:exc:])
        val2=val-32
        char=chr(val2)
        print(char,end="")
    inc+=1