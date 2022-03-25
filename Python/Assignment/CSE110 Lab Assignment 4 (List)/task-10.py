sr=input("Enter element: ")
sr=sr.split(",")
input_list=[]
modified_list=[]
for i in range(len(sr)): 
    if int(sr[i]) not in modified_list:
        modified_list.append(int(sr[i]))
    input_list.append(int(sr[i]))
print("Input list: ",input_list)
print("Modified list: ",modified_list)