#fucntions and parameter passing
# creating our own functions 

def  say_hello():
    print("hellooooooo worold!")


say_hello() #calling the function

#parameters

def say_hello(name, emoji):
    print(f' helloooo {name} {emoji}')


#arguments used when you pass value to a function

say_hello('keerthana', '😝') #call or invoke a funciton with arguments
say_hello('Johnson', '😊')
say_hello('Anthony', '😇')
 
#default parameters and keyword arguments

#positional arguemnts, the arguments must be in the same position as the function parameters

#keywork arguments 
#this what happens.

say_hello(emoji='🥳', name="Ziddu")



