
items =input("Enter a list of items: ")
location=input("Enter Location: ")
items = items .strip("[]")
sr=''
list1=''
for i in items:
    sr+=i
for j in sr:
    if j =='"':
        continue
    else:
        list1+=j
list1=list1.split(",")
def price_cal(var,loc):
    sum=0
    dict1={"Rice":105,"Potato":20,"Chicken":150,"Beef":510,"Oil":85}
    for x in var:
        for k,v in dict1.items():
                if k ==x:
                    sum+=v
                elif k ==x:
                    sum+=v
                elif k ==x:
                    sum+=v
                elif k ==x:
                    sum+=v
                elif k == x:
                    sum+=v
                else:
                    pass
    if loc=="Dhanmondi":
            sum+=30
    else:
            sum+=70
    print(sum)
price_cal(list1,location)