#class ---> keyword to define a new class
class Dog:
    #first define the common and then the unique
    #can be called a constructor
    #init is a method which can also be a constructor 
    #that runs everytime an object is created
    def _init_(self,name,age):
        self.name=name   #lucy
        self.age=age     #4 years

#dog has a barking nature
#behaviour of the parent class        
    def bark(self):
        #attributes unique to each instance od dog class
        return f"{self.name} doesm't bark!"
    
#objects : instance of a class dog
#dog1 is a dog
#dog2 is a dog
dog1=Dog("Lucy",4)
dog2=Dog("Lucy",3)
#as many number of dogs as per the requirement

dog1.bark()
dog2.bark()