# class buttons:
#     def __init__(self,word,spaces,border):
#         self.word = word
#         self.spaces = spaces
#         self.border = border
#         n1=(len(self.word))
#         spacebar = ' '*(self.spaces)
#         # for i in range(self.spaces):
#         #     spacebar+=" "
#         first = self.border*(n1+2+(self.spaces*2))
#         second = self.border + spacebar + self.word + spacebar + self.border
#      print(first)
#      print(second)
#      print(first)
# word = "CANCEL"
# spaces = 10
# border = 'x'
# b1 = buttons(word, spaces, border)print("=======================================================")
# b2 = buttons("Notify",3, '!')print("=======================================================")
# b3 = buttons('SAVE PROGRESS', 5, '$')
# class Student:
#     def __init__(self):
#         self.name = None
#         self.cgpa = 0.0
# s1 = Student()
# s2 = Student()
# s3 = None
# s1.name = "Student One"
# s1.cgpa = 2.3
# s3 = s1
# s2.name = "Student Two"
# s2.cgpa = s3.cgpa + 1
# s3.name = "New Student"print(s1.name)print(s2.name)print(s3.name)print(s1.cgpa)print(s2.cgpa)print(s3.cgpa)
# s3 = s2
# s1.name = "old student"
# s2.name = "older student"
# s3.name = "oldest student"
# s2.cgpa = s1.cgpa - s3.cgpa + 4.5print(s1.name)print(s2.name)print(s3.name)print(s1.cgpa)print(s2.cgpa)print(s3.cgpa)

# class Ninja:
#     def __init__(self):
#         self.rank = 0
#         self.stamina = 0.0

# naruto = Ninja()
# yellow_flash = Ninja()
# naruto.rank = 1
# naruto.stamina = 95.0
# print(naruto.rank)
# print(naruto.stamina)
# yellow_flash.stamina = naruto.stamina - 2
# print(yellow_flash.stamina)
# yellow_flash.rank += (naruto.rank + 1)
# print(yellow_flash.rank)
# minato = yellow_flash
# print(minato.rank)
# print(minato.stamina)
# naruto.rank = minato.rank - 1
# naruto.stamina = yellow_flash.stamina + 3
# print(naruto.rank)
# print(naruto.stamina)
# naruto.rank = -(-naruto.rank)
# yellow_flash.stamina = -(-minato.stamina)
# print(naruto.rank)
# print(minato.stamina)