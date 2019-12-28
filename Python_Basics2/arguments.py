#arguments

# *args and **kwargs, arguments and keyword arguments

#for multiple arguments use the symbol *

def super_functions(*args, **kwargs):
    print(kwargs)
    for items in kwargs.values():
        total += items
    print(args)
    return sum(args) + total

print(super_functions(1,2,3,4,5, num1=5, num2=10))


