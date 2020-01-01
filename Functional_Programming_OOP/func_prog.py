#functional Programming
# is all about separations or concerns so everything is organized based on functionaliity

# separate data and functions
# pure functions mean less buggy code
#functional Progrmming is all pure functions. 
#pure functions - given the same input... always return the same output. and a functioin should not produce side effects

#ALSO using lambda

def multiply_by2(li): #this function does not touch the outside world . it should not also interact with print or anything
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list



print(multiply_by2([1,2,3]))
#print(multiply_by2([1,2,3]))

#maps(), filtter, zip and reduce

#maps - returns a new list, for iterate over

my_list = [1,2,3]
your_list = [10,20,30]
their_list = [5,6,6]
def map_multiply_by2(item):
    return item*2


print(list(map(map_multiply_by2,my_list)))

print("multiply by 2 using lambda")
print(list(map(lambda item: item*2, my_list)))


#filter 

def only_odd(item): # if the number is odd keep it in the list, else remove
    return item % 2 != 0 #odd

print(list(filter(only_odd, my_list)))
 
#zip
#  need two lists to zip them together
# zip takes the 1 items from each list and adds to create a tupule
 
print(list(zip(my_list,your_list, their_list)))

#reduce
# reduce is not in the python built in functions, we have to use "from functools import reduce"

from functools import reduce

def accumulator(acc, item): #acc is default 0
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0)) #returns and prints the final value of the accumulator

#exercise

#map
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))

#zip

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings,sorted( my_numbers))))

#filter

scores = [73, 20, 65, 19, 76, 100, 88]

def above_fifty(score):
    return score > 50

print(list(filter(above_fifty, scores)))


#reduece

def accumulator1(acc, item):
    return acc + item

print(reduce(accumulator1, (my_numbers + scores)))

#lambda expressions - anonymous fucntions, only need once "lambda param: action(param)"

#exercise lambda 

my_list1 = [5,4,3]

print(list(map(lambda num:  num** 2, my_list1)))

#list sorting

a = [(0, 2), (5, 2), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1] )

print(a)