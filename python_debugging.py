#debugging in Python 
# the act of finding and removing bugs or errors from our code is called debugging

#linting
#use ide/editor
# read errors

#python debugger pdb module

import pdb

def add(num1, num2):
    pdb.set_trace() #it traces the input and output
    return num1 + num2

add(4, 5 )