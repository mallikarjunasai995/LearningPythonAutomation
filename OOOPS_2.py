# #inheritance #polymorphism #MRO
# #reddit - singup for account , base regular user but moderators will also be there
#has-a relationship - composition- compose bigger objects with small individual objects 
# (car honda city example- code reusability) - call the car object in employee object itself
#is-a relationship - inheritance
# #inheritance - ability to define a class which inherits from another class(base or parent class)
# #Inheritance works by passing the parent class as an argument to the child class - code extendibility
#code reusabillity
#single inheritance - concept of 1 class and 1 parent
#multilevel inheritance - inheriting classes from multiple classes grandparent --> parent --> child
#hiereichacla inheritance - inheriting multiple child classes from one multiple parent class
#multiple inheritance - oone child class inherting multiple parent classes 
#cyclic inheritance - not supported by python/java

#method resolution order - in which order hybrid inheritent classess should execute 
##################### ------> (classname.mro())

#innterclasses - class within class .. class universtity and class department .. 
#                 without existing university class there won't be department classs
#create instance of innter object ---      x = outerobject() , y = x.innterobject() , y.m1()



#nested methods to avoid the repetition of the code

# class Human:
#     def __init__(self,first,last,age):
#         self.first = first
#         self.last = last
#         self.age = age
#         # if age >=0 : 
#         #     self._age = age #here _age represents a private variable
#     # def get_age(self):
#     #     return self._age
#     # def set_age(self,new_age):
#     #     if new_age >=0:
#     #         self._age = new_age
#     #     else:
#     #         raise ValueError("age can't be negative")

# #instead of setter , getter methods - we use (check below line)
# # properties - we can call directly the function name without params
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self,value):
#         if value>= 0:
#             self._age = value
#         else:
#             self._age = 0



# jane = Human("jane", "godall",28)
# # print(jane.get_age())
# print(jane.age)
# jane.age = 43
# print(jane.age)


#superclass lecturer


class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

   

class Cat(Animal):
    def __init__(self, name, species,breed,toy):
        super().__init__(name, species)
        self.breed = breed
        self.toy = toy

    def __repr__(self):
        return f"{self.name} is a {self.species} and likes the toy {self.toy}"

        

Meow = Cat('meow','smalllion','kuttilion','beblade')
print(Meow)


#multiple inheritance - getting access to methiods from multiple classes - Class Penguin(Ambulartory,Aquatic) --- here first one which is amubulatory has a preference and 
#calls when init happens as a super method , order is important
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#Polymorphism - 
#   1. same class method works in a similar way for different classes 
#   2. common use case is method overriding - method in base class is overriden by subclass
# same opertion works for differnt kinds of objects -- example special methods which is shown below

#operator   overloading - same operator can be used for multiple operations 
#example - + operator in python - print(2+2), print(durga***3)
#can't use objects addition with + operator , but magic method can be used __add__()

#__str__()  : whenever we use print fucntion , internally it will call default string format method will be called

#method overloading - not supported in python - same method name but different argument types- in python 
###################### -- only last method will execute because we can't delcare type explicity - dynamic overloading


#(if child class not satisfied with the params of parent class then we redefine child class method is called
## method overriding)


class Human: 
    def __init__(self, height):
        self.height = height
    def __len__(self):
        return self.height
    def __repr__(self):
        return str(self.height)
m = Human(60)
print(m)
print(len(m))




#grumpydict

class GrumpyDict(dict):
    def __repr__(self):
        print('none of your business')
        return super().__repr__()
    def __missing__(self, key):
        pass




data = GrumpyDict({"name":"malli","age":"26"})
print(data)





#garbage collector - to destroy the useless objects that are filled in the memory
#by default , GC is enabled ... 
#gc module  - gc.enable(), gc.isenable() , gc.disable()
#destructor = __del__() -- special method to clean up activities (resource deallocation act. ) opp. to constructor (__init__)
#t1 = None (object elitble for gc)
