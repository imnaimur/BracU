string=input("Enter a string: ")
count=0
index=0
i=0
while i<(len(string)):
    value=ord(string[index:count+1:])
    if value == 48 or value ==49:
         count+=1
         index+=1
         checking=True
    else:
        print("Not a Binary Number")
        break
    i+=1
if value == 48 or value ==49:
    print("Binary Number")