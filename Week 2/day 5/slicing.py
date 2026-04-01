#slicing-substring

myString="abcdef ghijkl"
sub1=myString[0:6] #slice the first element
sub2=myString[7:] #from the 7th element till end
sub3=myString[:5] #first 6 elements
sub4=myString[10] #the 10th element - index from 0
sub5=myString[-5] #last 5 elements

if "a" in myString:
    print("a is there")

word = myString.split(" ")
print(word)

#---inbuilt funtions---

myString.upper()
myString.lower()

#append is used in collaboration and avoided in string
#print(myString+ "m")

myString = myString+ "m"
print(myString)
#the above string is not same and a new string created 
#string is immutable in python