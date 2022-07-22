
# task-1
# string = input()
# count1 = 0
# count2 = 0
# for x in string:
#     if 'A' <= x <= 'Z':
#         count1 += 1
#     else:
#         count2 += 1
# if count1 > count2:
#     print(string.upper())
# else:
#     print(string.lower())


# Task-2
# string=input()
# number=False
# word=False
# for x in string:
#   if "0"<=x<="9":
#     number=True
#   else:
#     word=True
# if number==True and word==True:
#   print("Mixed")
# elif number==True:
#   print("Number")
# else:
#   print("Word")


# task-3
# s = input()
# s1 = ""
# count = 0
# for x in s:
#     if 'A' <= x <= 'Z':
#         count += 1
#     elif count == 2:
#         break
#     elif count == 1:
#         s1 += x
#     # else:
#     #     pass
# if len(s1) == 0:
#     print("Blank")
# else:
#     print(s1)


# task-4
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
