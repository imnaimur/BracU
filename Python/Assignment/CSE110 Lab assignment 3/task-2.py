string=input("Enter a string: ")
index=int(input("Enter a index: "))
if len(string)>1:
    print(string[index::-1],end="")
    print(string[index+1::])