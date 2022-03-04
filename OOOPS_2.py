# #inheritance #polymorphism #MRO
# #reddit - singup for account , base regular user but moderators will also be there

# #inheritance - ability to define a class which inherits from another class(base or parent class)
# #Inheritance works by passing the parent class as an argument to the child class


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

