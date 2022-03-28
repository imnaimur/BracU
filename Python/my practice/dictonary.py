dict1={1:"red",2:"blue",3:"green","number":[1,2,3,4,5],5:500,"2g":[["mi","xiaomi"],"realme","samsung","iphone"]}
# dictonary's mutability
# dict1["2g"]="asus"
print(dict1.get("2g",["invalid keywords"]))
print(type(dict1[5]))