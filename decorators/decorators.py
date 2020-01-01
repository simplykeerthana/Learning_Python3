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

