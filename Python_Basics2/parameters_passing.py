#fucntions and parameter passing
# creating our own functions 

def  say_hello():
    print("hellooooooo world!")


say_hello() #calling the function

#parameters

def say_hello(name = 'Keerthana', emoji = '😜'):
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

say_hello()



# return statements in fucntions 

def sum(num1, num2):
   return num1 + num2 #you must have the return statement to return something or else it's gonna return none

print(sum(1,3))

total = sum(10,5)
print(sum(10,total)) #you can also send in variables to the function


#nested functions

def sum1(num1, num2):
    def another_func(n1, n2): # this function does not get called
        return n1 + n2  
    return another_func(num1, num2) # so you have to 


total1 = sum1(10,20)

print(total1)



#telsa exercise, you just got employed by Tesla and solve a problem and you need to solve a problem for their self driving car

age = input("What is your age?: ")


def checkDriverAge(age = 0):
   
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratualations on your first year of driving. Enjoy the ride!")
    

checkDriverAge(age)

#DocStrings

def test(a):
    '''
    Info: this function test and prints param a 
    '''
    print(a)


test('!!!!')

# use help() to know what a function does
 
 # help(test)

 # __doc__ for doc strings, you print those doc strings to the screen

print(test.__doc__)

#clean code

 #not clean code

 def is_even(num):
     if num % 2 == 0:
         return True
      elif num % 2 != 0:
          return False 

print("Not so clean code")
print(is_even(51))