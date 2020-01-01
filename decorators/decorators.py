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
    def wrap_func(*args, **kwargs):
        print('************')
        func(*args, **kwargs)
        print('************')
    return wrap_func

@my_decorator
def hello1(greeting, emoji = ':)'):
    print(greeting, emoji)

@my_decorator
def bye():
    print('goodbye 2019')

hello1('hiiii')
bye()

#practical applications of decorator

#module time
from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2  = time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper

@performance 
def long_tiime():
    for i in range(10000000):
        i*5

long_tiime()


#authentication

user1 = {
    'name': 'sorna',
    'valid': True
}

def authentication(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper

@authentication

def message_friends(user):
    print('message has been sent')

message_friends(user1)

