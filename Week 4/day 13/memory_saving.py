def large_num(n):
    for i in range(n):
        yield i

#this doesn't create a lakh numbers in memory
gen=large_num(100000)
print(next(gen))
print(next(gen))
print(next(gen))

#basic list comprehension
list=[x*x for x in range(5)]
print(list)

#doing comprehension using generator 
gen=[x*x for x in range(5)]
print(gen)