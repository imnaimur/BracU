# b="BANGLA"
# for i in range(len(b)):
#     for j in range(i+1):
#         print(b[j],end="")

#     print()
# a="+"
# n=2
# for i in range(n):
#     for j in range(n):
#         print(a,end="")
#     print()
# i = 0
# while True:
#     print(i)
#     if i==20:
#         break
#     i+=1
# dic={1:"good",2:"bad"}
# dic.update({"naimur":22101075})
# for i,j in dic.items():
#     print(i,j)
# l=["mangoes","bananas","papayas",["king","queen"],"barries"]
# l.insert(2,"guavas")
# l[1]="carrot"
# print(l)
# def dj(*a):
#     b,c,d,e=a
#     print(b,c,d,e)
# dj("google","Samsung","Apple","Xiaomi")
# print(ord("Z"))
# s="bANGLAdESH"
# p=''

# for i in s:
#     if 90>= ord(i)>=65:
#         a=chr(ord(i)+32)
#         p+=a
#         pass
#     else:
#         a=chr(ord(i)-32)
#         p+=a
# print(p)
# s = "baNgladEsh"
# s1 = ""
# count=0
# for x in range(len(s)):
#     if 'A'<= s[x] <= 'Z':
#         count+=1
#     elif count==2:
#         break
#     else:
#         s1+=s[x]
# print(s1)
# string1  = input()
# string2 = input()
# string3 = ""
# for char in string1:
#     if char in string2:
#         string3 += char
# for char in string2:
#     if char in string1:
#         string3 += char
# print(string3)


# uc="(_ , $ , #, @)"
# password=input()
# lowercase=False
# uppercase=False
# digit=False
# uni=False
# for x in password:
#   if 'A'<=x<='Z':
#     uppercase=True
#   elif 'a'<=x<='z':
#     lowercase=True
#   elif x in uc:
#     uni=True
#   else:
#     digit=True
# if lowercase ==True and uppercase==True and uni ==True and digit==True:
#   print('OK')

# if uppercase ==False:
#         print("Uppercase character missing")
# if lowercase==False:
#         print("Lowercase character missing")
# if digit==False:
#         print("Digit missing")
# if uni ==False:
#         print("Special character missing")

#2 no.
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

#1 no.
# i = 0
# list1 = []
# list2 = []
# while True:
#     n = input()
#     if n == "STOP":
#         break
#     list1.append(int(n))
# for j in list1:
# 	if j not in list2:
# 		list2.append(j)
# 		print(j,end = "-")
# 		print(list1.count(j),"times")



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

# 4 no.
# first_input = input("Enter n and k: ")
# first_input = first_input.split()
# k = int(first_input[1])
# second_input = input("Enter perticipate times: ")
# second_input = second_input.split()
# eligible = []
# for i in range(int(first_input[0])):
#     if int(second_input[i])+k <= 5:
#         eligible.append(int(second_input[i]))
# print(len(eligible)//3)


# dict
#1no
# def dict_make(dictionary):
#     dictionary = dictionary.split(",")
#     dict1={}
#     key = []
#     value = []
#     for i in dictionary:
#         for j in i:
#             if j == ":":
#                 key.append(i[:i.index(":"):])
#                 value.append(i[i.index(":")+1::])
#     for i in range(len(key)):
#         dict1.update({key[i]:int(value[i])})
#     return dict1
# s1 = 'a: 100, b: 100, c: 200, d: 300'
# s2 = 'a: 300, b: 200, d: 400, e: 200'
# dict1 = dict_make(s1)
# dict2 = dict_make(s2)
# dict3 = {}
# faka_list=[]
# for i in dict1:
#     if i in dict2:
#         dict3[i] = dict1[i]+dict2[i]
#     else:
#         dict3[i] = dict1[i]
# for j in dict2:
#     if j not in dict3:
#         dict3[j] = dict2[j]
# for k in dict3.values():
#     if k not in faka_list:
#         faka_list.append(k)
# print(dict3)
# faka_list = sorted(faka_list)
# faka_list = tuple(faka_list)
# print("values",faka_list)


#2NO.
# i = 0
# list1=[]
# list2 = []
# dicto = {}
# while True:
#     n = input()
#     if n == "STOP":
#         break
#     list1.append(int(n))
# list1 = sorted(list1)
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#         dicto.update({i:list1.count(i)})
# # print(dicto)
# for i,j in dicto.items():
#     print(f"{i} - {j} times")

# 3 NO
# dicto={'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value1'}
# dicto2={}
# for i in dicto:
#     if dicto[i] in dicto2:
#         dicto2[dicto[i]].append(i)
#     else:
#         dicto2.update({dicto[i]:[i]})
# print(dicto2)

# keypad = {0:" ",1:['.',',','?','!',':'],2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z']}
# string = 'Hello, World!'
# string = string.upper()
# string2 = ''
# for k in string:
#     for i,j in keypad.items():
#             if k in j:
#                 string2 += str(i)*(j.index(k)+1)
# print(string2)



#Function


# def bmi_cal():
#     string = input("Enter hight and weight: ")
#     string = string.strip("()")
#     string = string.split(",")
#     h = int(string[0])/100
#     w = int(string[1])
#     bmi = w/(h**2)
#     if bmi<18.5:
#         print(f"Score is {'%.1f'%bmi}.You are Underweight")
#     elif 18.5<= bmi <= 24.9:
#         print(f"Score is {'%.1f'%bmi}.You are Normal")
#     elif 25<= bmi <=30:
#         print(f"Score is {'%.1f'%bmi}.You are Overwight")
#     else:
#         print(f"Score is {'%.1f'%bmi}.You are Obes")
# bmi_cal()



#2
# def div_cal(inc,exc,div):
#     sum = 0
#     for i in range(inc,exc):
#         if i %div == 0:
#             sum += i
#     print(sum)
#     pass

# arg = input("Enter arguement: ")
# arg = arg.split(',')
# result = div_cal(int(arg[0]),int(arg[1]),int(arg[2]))


# 3
# BBQ Chicken Cheese Burger 250
# Beef Burger 170
# Naga Drums 200
# def orde_price(location='Mohakhali'):
#     order = input("Enter order and location: ")
#     order = order.split(',')
#     location='Mohakhali'
#     if len(order)==2:
#         location = order[1]
#     menu = {"BBQ Chicken Cheese Burger":250,"Beef Burger":170,"Naga Drums":200}
#     price = 0
#     for i,j in menu.items():
#         if order[0] in i:
#             price+=j
#     if location == 'Mohakhali':
#         location = 40
#     else:
#         location = 60
    
#     price += price*(8/100)
#     price += location
#     print(price)
# result = orde_price()

#4
# alice@kaaj.com,sheba.xyz,kaaj.com
# def changer():
#     string = input()
#     string = string.split(",")
#     string2=''
#     if len(string) ==3:
#         for i in string[0]:
#             string2 += i
#             if i == "@":
#                 break
#         string2 += string[1]
#         print("Changed:",string2)
#     else:
#         print("Unchanged:",string[0])

#5
# changer()
# def palindrome(s):
#     s1=''
#     for i in s:
#         if i == " ":
#             pass
#         else:
#             s1 += i
#     s2 = s1[::-1]
#     if s1 == s2:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")
# s = input(" enter string: ")
# palindrome(s)


# string ="my favourite animal is a dog.a dog has sharp teeth so that it can eat flesh very easily.do you know my pet dog’s name?i love my pet very much."
# def correct(string):
#     string2 = ''
#     first_letter = chr(ord(string[0])-32)
#     string2 += first_letter
#     for i in range(1,len(string2)):
#         if string[i] == '.':
#             print('run')
#             string2 += chr(ord(string[i+1])-32)
#     print(string2)
# correct(string)
