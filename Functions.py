def auto_tune():
  return "singers will mostly do autotune when in pubic stages"
-------------------------------------------
#parameters in functions
def square(num):
  return num*num
squre(4)
--------------------------------------------
def yell(word):
    return f"{word.upper()}!"
 ---------------------------- ----------------
#default parameters
def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"
--------------------------------------------
  #keywordArguments
  #diff b/n keyword args and default paramters
  
  
