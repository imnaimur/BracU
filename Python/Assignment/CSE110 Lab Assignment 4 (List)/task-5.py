# ["hey", "there", "", "what's", "", "up", "", "?"]
#Original List: ['hey', 'there', '', "what's", '', 'up', '', '?']
# Modified List: ['hey', 'there', "what's", 'up', '?'] 
string=input("Enter string: ")
string=string.split(",")
modified_list=[]
print(string)
for i in string:
    if i!="":
        modified_list.append(i)
print("Original List: ",string)
print("Modified List: ",modified_list)