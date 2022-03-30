list1=[2,7,12,17,18,88,58,7,89,78,74,55,33,57]
new_list1=[]
new_list2=[]
final_list=[]
index=0
for i in range(len(list1)):
  if i%2==0:
    new_list1.append(list1[i])
  else:
    new_list2.append(list1[i])
for j in new_list1:
  index-=1
  final_list.append(j+new_list2[index])
print("New list one: ",new_list1)
print("New list two: ",new_list2)
print("The final list: ",final_list)