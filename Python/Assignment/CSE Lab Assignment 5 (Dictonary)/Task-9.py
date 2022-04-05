exam_marks ={'Cierra Vega':175, 'Alden Cantrell':200, 'Kierra Gentry':165, 'Pierre Cox':190}
n=int(input("Enter marks: "))
dict1={}
for i,j in exam_marks.items():
    print(j)
    if j>=n:
        dict1.update({i:j})
print(dict1)