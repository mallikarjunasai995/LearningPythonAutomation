#OOOPS........ #classes/objects
#__ - underscore before any method represents private methods
#Encapsulation - the grouping lo public and private attributes and methods into a programmatic class, making abstraction possible
#Example - Designing a deck class , make cards a private attribute(list)
#Abstraction - idea to expose only relavant data in class interface hiding private attributes and methods
#classnames - CamelCase
#methodnames/Variables - snakeCase
#__init__(self,x,x) - is like constructor for a class aka default method
#self keyword refers to the current class of an instance
# Define Bank Account Below:
# class BankAccount:
#     def __init__(self,owner):
#         self.owner = owner
#         self.balance = 0.0
        
#     def balance(self):
#         return self.balance
    
#     def deposit(self,amount):
        
#         self.balance = self.balance + amount
#         return self.balance
    
#     def withdraw(self,amount):
        
#         self.balance = self.balance - amount
#         return self.balance
        



"""importnace of class attributes- idependent of instance methods and apply to the whole class

"""
class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0
    
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs

hen1 = Chicken("natukodi","kodi")
hen2 = Chicken("normalkodi","kodi")

"""Class methods : @class method decorator , concerned with the class itself
   cls - keyowrd as like self in instance methods 
   def(cls, data_stirng):
       first,second,thrid = data_string.split(",")

    we will on use this when we reflect the change on entire class level rather on isntances

"""

"""
dunder __repr__ method : representation
 while printing the object , we get object at particular memory address 
 isntead repr method will give us the exact info depends on what we return
 inside that ...

"""


