#iteratoranditerable

#iter and #iterable
#example : for i in [1,2,3]
#inside that for loop .. we call iter on list of [1,2,3] and again calls next until the iter object ends
#iter()
#next()
def my_for(iterable,func):
    iterator = iter(iterable)
    try:
        thing = next(iterator)
    except StopIteration:
        print("hey this loop is done")
    else:
        func(thing)

    
my_for('hello',print)

#generator - Yeild count  -- Yeild is the keyword
#generator will take less memory and less time 
#yield is the keyword