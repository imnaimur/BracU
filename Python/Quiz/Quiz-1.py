i=0
counter=0
ammount=0
while i<5:
    number=input("Enter a number: ")
    if number=="End":
        break
    ammount+=1
    num=int(number)
    if num%2!=0:
        counter+=1
    i-=1
print(int((counter/ammount)*100),"percent Zombies")