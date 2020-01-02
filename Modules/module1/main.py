#modules in python, many files in one dirctory
# to  link multiple .py files into one modules. 

# to communicate with the utility file use import command

#a folder in python is a pacake


#import utility #you can import many files

#import shopping_cart, this won't work because shopping_cart is not a module

from utility import multiply, diivide
#import Shopping.more_shopping.shopping_cart
from Shopping.more_shopping.shopping_cart import buy #just import the buy fucntion

#print(utility) #when you run this statement, python generates a py cache folder 

if __name__ == '__main__':
    print(diivide(2,3))
    print(multiply(2,3))
    print(buy('apple'))
    print(buy('banana'))
#to save time, python is going to run the cache file next next time utility is called if there is no change made to the program

#print(Shopping.more_shopping.shopping_cart.buy('apple')) # you have access to shopping_cart module

#print(Shopping.more_shopping.shopping_cart.buy('banana'))




# a python package creattes an __int__.py automatically, it may or may not be hidden by the IDE

#Python modules are like standard library, there are tons of libraries to use, like email, math, stats and etc

import random

print(random)  

#help(random) is like man pages
#dir(random) shows all the method random has

print(random.random()) #is gonna give us a random number from 0 and 1

print(random.randint(1,10))

print(random.choice([1,2,3,4,5])) #makes a choice to print a element from the list

my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

#sys module

import sys
print(sys)

sys.argv

# use sys module to create a guessing name, argv --> input from terminal

