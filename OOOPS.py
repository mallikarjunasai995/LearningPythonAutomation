#OOOPS........ #classes/objects
# everything in python is object which has attributes and methods(nothing but functions in the class)
#__ - underscore before any method represents private methods
#Encapsulation - the grouping lo public and private attributes and methods into a programmatic class, making abstraction possible
#Example - Designing a deck class , make cards a private attribute(list)
#Abstraction - idea to expose only relavant data in class interface hiding private attributes and methods
#classnames - CamelCase
#methodnames/Variables - snakeCase
#__init__(self,x,x) - is like constructor for a class aka default method
#self keyword refers to the current class of an instance


#python will create a class level object using PVM for every object
#static , instance , local variables 
#static method - general utility method @static method decorator (not using static or instance variables)
#instance method - insdie method if we are accessing instance variable is called instance method - first argument is self
#class method - @class method decorator we need to put , mostly we will use to access static methods within a class by passing
               #cls variable



# Accessing attributes and methods of one class in another class --
# answer)) create parent object first then pass the parent object (not class ) to another class whcih needs that
# Accessing Attributes and Methods in Python -- ??




#polymorphism - operator overloading . example -- + operator used to concatenate ints and strings as well
                # method overriding - child class has same method like parent but with some modification


#abstraction - abstract method -only declaration bt not engouh implementation
            # declare abstract method by using @abstractmethod decorator
            #abstractmethod present in abc module - ABC - abstract base class
            #abstract class contians both abstract and non abstract methods
#interface - only contains abstract methods - service requriement specification - SRS

from abc import abstractmethod
class Vehicle:
    @abstractmethod
    def getNoofWheels(self):
        pass


#abstract class - class contains abstract methods

# __variable - privare variable similary private method can also be declare but through "name manglign" we can access these also

#_protected  - (single underscore) - within the class you can access like private member also 
                # outside of class only in child class you can accesss


#data hiding - declare private member for the variable which shouldn't be seen  - example - bank - bank balance
                #some validation/authentication method then return the private member variable through that method in the class
                



# class student:
#     schoolname = 'durgasoft'
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#     def getStudentInfo(self): #instance method
#         print("student name : "+ self.name)

#     @classmethod
#     def getSchoolName(cls):
#         print("class static variable "+ cls.schoolname)
    
#     @staticmethod
#     def getsum(a,b):
#         sum = a+b
#         return sum

# delete,access instance and static varianles : 






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


