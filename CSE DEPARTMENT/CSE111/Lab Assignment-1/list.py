# 1 no.
# i = 0
# list1 = []
# list2 = []
# while True:
#     n = input()
#     if n == "STOP":
#         break
#     list1.append(int(n))
# for j in list1:
#     if j not in list2:
#         list2.append(j)
#         print(j, end="-")
#         print(list1.count(j), "times")

#----------------------------------------------------------------------------------------

# 2 no.
# n=int(input("enter list number: "))
# container=[]
# sum_cont=[]
# count=0
# for i in range(n):
#     list2=[]
#     list1=input("enter list: ")
#     list1=list1.split()
#     for item in list1:
#         list2.append(int(item))
#     container.append(list2)
# for j in range(len(container)):
#     sum=0
#     for k in container[j]:
#         sum+=int(k)
#     sum_cont.append(sum)
# max=sum_cont[0]
# for total in sum_cont:
#     if max<total:
#         max=total
#         count+=1
# print(max)
# print(container[count])

#----------------------------------------------------------------------------------------

# # 3 no.
# import math
# container = []
# sum_con = []
# while True:
# 	list1 = []
# 	string=input()
# 	if string == "STOP":
# 		break
# 	else:
# 		string=string.split()
# 		for i in string:
# 			list1.append(int(i))
# 		container.append(list1)
# for j in range(len(container)):
# 	list2 = []
# 	n = len(container[j])
# 	for k in range(n-1):
# 		sum = abs(container[j][k]-container[j][k+1])
# 		list2.append(sum)
# 	list2 = sorted(list2)
# 	n1 = len(list2)
# 	ub_jumper = False
# 	for ix in range(1,n1):
# 		if ix == list2[ix-1]:
# 			ub_jumper = True
# 		else:
# 			ub_jumper = False
# 			break
# 	if ub_jumper == True:
# 		print("UB Jumper")
# 	else:
# 		print("Not UB Jumper")

#----------------------------------------------------------------------------------------

# 4 no.
# first_input = input("Enter n and k: ")
# first_input = first_input.split()
# k = int(first_input[1])
# second_input = input("Enter participate times: ")
# second_input = second_input.split()
# eligible = []
# for i in range(int(first_input[0])):
#     if int(second_input[i])+k <= 5:
#         eligible.append(int(second_input[i]))
# print(len(eligible)//3)
