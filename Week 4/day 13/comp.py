#dict comprehension
d={num:num*2 for num in range(1,4)}

states = ['kerala','tamilnadu','karnataka']
capitals = ['thiruvananthapuram','chennai','bangalore']

di ={states:capitals for states,capitals in zip(states,capitals)}

#set comprehension
a=[1,1,2,2,5,3,7,5]
s={n for n in a if n%2 ==0}
print(s)