#decorators, have the @ sign and a name following it

def hello(func):
    #print('hell00000000')
    func()



#greet = hello

#del hello #delete the name hello, but the function can't be deleted because greet is pointing to it

def greet(): 
    print('still here!')
 
a = hello(greet)

print(a)

# @decorator supercharges our function to have some extra features

#high order decorator HOC
# accepts a function as its parameter
# or returns a function

def greet1(func): # a fuction tha accepts another function
    func()

def greet2():
    def func():
        return 5
    return func

#write our own decorator




def my_decorator(func):
    def wrap_func():
        func()
    return wrap_func

@my_decorator
def hello1():
    print('helloooo')

hello()