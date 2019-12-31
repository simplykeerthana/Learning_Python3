#functional Programming
# is all about separations or concerns so everything is organized based on functionaliity

# separate data and functions
# pure functions mean less buggy code
#functional Progrmming is all pure functions. 
#pure functions - given the same input... always return the same output. and a functioin should not produce side effects

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


#filter 

def only_odd(item): # if the number is odd keep it in the list, else remove
    return item % 2 != 0 #odd

print(list(filter(only_odd, my_list)))
 
#zip, need two lists to zip them together
# zip takes the 1 items from each list and adds to create a tupule
 
print(list(zip(my_list,your_list, their_list)))


