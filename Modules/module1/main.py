#modules in python, many files in one dirctory
# to  link multiple .py files into one modules. 

# to communicate with the utility file use import command

#a folder in python is a pacake


import utility #you can import many files
#import shopping_cart, this won't work because shopping_cart is not a module

import Shopping

print(utility) #when you run this statement, python generates a py cache folder 

print(utility.diivide(2,3))
print(utility.multiply(2,3))
#to save time, python is going to run the cache file next next time utility is called if there is no change made to the program

 print(Shopping.shopping_cart)