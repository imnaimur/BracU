def data(given_tuple):
    dict1 = dict(given_tuple)
    dict2= {}
    dict3 = {}
    # print(dict1)
    for i,j in dict1.items():
        string = ""
        string+=i
        j = str(j)
        if j[3:5] == '01':
            dict2.update({'Gillian flynn':string})
            if int(j[5:]) <50:
                    dict2['Gillian flynn']+='-poor'
            elif 50<= int(j[5:]) <= 85:
                    dict2['Gillian flynn'] += '-moderate'
            else:
                    dict2['Gillian flynn'] += '-excelent'
        else:
            dict2.update({'Stphen king':string})
            if int(j[5:]) <50:
                    dict2['Stphen king']+='-poor'
            elif 50<= int(j[5:]) <= 85:
                    dict2['Stphen king'] += '-moderate'
            else:
                    dict2['Stphen king'] += '-excelent'

        
                
    print(dict2)
    # for x,y in dict2.items():
    #     y = tuple(y)
    #     dict3.update({x:y})
    # print(dict3)    
s = (('gine girl',1010135),('carrie',10202100),('the shining',1020277))
data(s)