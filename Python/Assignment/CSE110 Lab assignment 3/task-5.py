string=input("Enter a string: ")
exc=0
#exc for excluded index
for count in range(len(string)):
    exc+=1
    print(string[:exc:])    