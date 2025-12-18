myset = {"apple", "banana", "pomegranate", "apple", False, 0, 2}
mylist = ['a', 'b']
myset2 = {"m", "n"}
print(mylist)

empty_set=set()
empty_dict={ }
print(type (myset)) #data type

myset.add(10)
myset.discard(10)
myset.update(mylist)
mylist.append("grapes")

count = len(myset)
print(myset|myset2) #union
print(myset&myset2) #intersection

for fruit in myset:
    print(fruit)

#true = 1 (dublicate)
#false = 0 (dublicate)

#in keyword
#lhs of in is a subset of rhs of in