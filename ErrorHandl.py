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
    finally:
        print("Obviously I came to this point")
divide(1,0)