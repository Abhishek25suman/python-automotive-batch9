# class ---> keyword to define a new class
class Dog:
    # first define the common and then the unique
    # can be called a constructor
    # __init__ is a method which acts as a constructor
    # that runs every time an object is created
    def __init__(self, name, age):
        self.name = name   # Lucy
        self.age = age     # age in years

    # dog has a barking nature
    # behaviour of the parent class        
    def bark(self):
        # attributes unique to each instance of dog class
        return f"{self.name} doesn't bark!"

# objects : instance of a class Dog
# dog1 is a dog
# dog2 is a dog
dog1 = Dog("Lucy", 4)
dog2 = Dog("Tom", 3)
# as many number of dogs as per the requirement

print(dog1.bark())
print(dog2.bark())
