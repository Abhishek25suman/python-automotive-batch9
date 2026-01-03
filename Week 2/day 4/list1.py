#List = it is used to store multiple items in a single variable

brand =["iphone", "samsung", "oneplus", "nothing", "vivo"]
print(brand[0]) 
print(brand[2]) 
brand[0]="motorola"
print(brand[0]) #updated
brand.append("realme")
print (brand)
brand.remove("oneplus")
print (brand)
brand.pop() #remove last element
print (brand)
brand.pop(3) #remove element indexwise
print (brand)
brand.insert(0, "xiaomi")
print(brand)
brand.sort() #arrange alphabetically
print(brand)
brand.clear() #clear list
for i in brand:
    print(i)
