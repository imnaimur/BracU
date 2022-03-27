sr=input("Enter element separated by spaces: ")
# 7 12 4 55 96 2 11 61 33 42
# sr=sr.split()
modified_list=[]
original_list=[]
start=0
end=0
index=0
# for i in range(len(sr)):
#     if int(sr[i])%2==0:
#        modified_list.append(int(sr[i]))
#     original_list.append(int(sr[i]))
# print("Original list: ",original_list)
# print("Modified list",modified_list)
# print(sr)
for i in sr:
    if i==" ":
        end=index
        original_list.append(int(sr[start:end]))
        start=end+1
    index+=1
for j in original_list:
    if j%2!=0:
        modified_list.append(j)
print(original_list)
print(modified_list)