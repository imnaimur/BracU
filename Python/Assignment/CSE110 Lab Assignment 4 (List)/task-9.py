sr=input("Enter element: ")
sr=sr.split()
modified_list=[]
original_list=[]
for i in range(len(sr)):
    if int(sr[i])%2==0:
       modified_list.append(int(sr[i]))
    original_list.append(int(sr[i]))
print("Original list: ",original_list)
print("Modified list",modified_list)
print(sr)