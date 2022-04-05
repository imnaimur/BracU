Given_tuple=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
n=int(input("Entre number: "))
count=0
for i in Given_tuple:
    if n==i:
        count+=1
print(f"{n} appears {count} times in the tuple")