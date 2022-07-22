#1no
# def dict_make(dictionary):
#     dictionary = dictionary.strip("{}")
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
# s1 = input("Enter dictionary: ")
# s2 = input("Enter dictionary: ")
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
 