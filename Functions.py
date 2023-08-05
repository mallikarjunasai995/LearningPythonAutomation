# def auto_tune():
#   return "singers will mostly do autotune when in pubic stages"
# '''-------------------------------------------'''
# #parameters in functions
# def square(num):
#   return num*num
# square(4)
# '''-------------------------------------------'''
# def yell(word):
#     return f"{word.upper()}!"
# '''-------------------------------------------'''
# #default parameters
# def speak(animal="dog"):
#     noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
#     noise = noises.get(animal)
#     if noise:
#         return noise
#     return "?"
# '''-------------------------------------------'''
#   #keywordArguments
#   #diff b/n keyword args and default paramters
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print ("%s == %s" %(key, value))
 
# # Driver code
# myFun(first ='Geeks', mid ='for', last='Geeks')   

# def myfun(*argv):
#   for item in argv:
#     print(item)

# myfun('mallik','hasty')


#lambda fucntion - nameless 
triple = lambda x:x*3
print(triple(3))

#variable length arugments