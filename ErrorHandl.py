print("hi")
def colorize(text, color):
    if type(text) is not str:
        #comment-firstdebugerrorhandling,valueerror
        raise TypeError("text must be instance of str")
    print(f"Printed {text} in {color}",text,color)
colorize("hello","red")
#try,except,finally
d = {"1":"am first"}
def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
    

#get(d,"asdf")

def divide(a,b):
    try: 
        print(f"{a/b}")
    except (TypeError,ValueError,ZeroDivisionError) as err:
        print(err)
    except:
        print("base class exception thrown")
    finally:
        print("Obviously I came to this point")
divide(1,0)

#raise error 
def exception_raising_fn(switch):
    if swtich==1:
        raise valueError("Value specified was wrong")
    else switch ==2:
        raise NameError("Identifier not defined in the local or global scope")
    else:
        print("executed without exceptions")
        
try:
    exception_raising_fn(1)
except valueError as ve:
    print("OOPS a value Erros was thrown!", ve)
    print("Error type", type(ve))
    
finally:
    print("always executes"