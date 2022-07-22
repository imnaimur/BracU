# 1
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
#
# 2
# def div_cal(inc,exc,div):
#     sum = 0
#     for i in range(inc,exc):
#         if i %div == 0:
#             sum += i
#     print(sum)
#     pass
#
# arg = input("Enter arguement: ")
# arg = arg.split(',')
# result = div_cal(int(arg[0]),int(arg[1]),int(arg[2]))
#
# 3
# def orde_price(location='Mohakhali'):
#     order = input("Enter order and location: ")
#     order = order.split(',')
#     location = 'Mohakhali'
#     if len(order) == 2:
#         location = order[1]
#     menu = {"BBQ Chicken Cheese Burger": 250, "Beef Burger": 170, "Naga Drums": 200}
#     price = 0
#     for i, j in menu.items():
#         if order[0] in i:
#             price += j
#     if location == 'Mohakhali':
#         location = 40
#     else:
#         location = 60
#
#     price += price * (8 / 100)
#     price += location
#     print(price)
#
#
# result = orde_price()
#
# 4
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
# changer()
#
# 5
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
#
