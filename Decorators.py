#highorderfunctions

#functions that can pass into another functions and parameter of paraent function can be directly used
#in child function (which is insdie the parent function)
# def shout(fn):
#     def wrapper(*args,**kwargs):
#         return  fn(*args,**kwargs).upper()
#     return wrapper

# @shout
# def order(main,side):
#     return f"I would like to order {main} and one {side} dish"

# print(order("frenchfires","meal"))

#-------------------------------------------------------------------------
#------------------------------------------------------------------------

#wraps the functions and helping with metdef star(func):
from functools import wraps
from time import time

def star(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("*" * 30)
        print("executing the function {fn.__name__}")
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        print("executi the function {fn.__name__}")
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")


from functools import wraps
 
def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrappers