#python dictionary
# a dictionary has a key, value

dictionary = {
    'a':1,
    'b':2
}

print(dictionary['b']) #grabs the value of the key 

# a dictionary is an unordered key value pair. we just need the key to grab the values

# when shoud you use a list and dictionary
# unordered , key, value pairs-> dictionary
#ordered -> lisgs


# a dictiinary key needs to be immutable
# a value that is not change
# also a key in dictionary should be unique


#dictionary methods. 


user = {

    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

print(user.get('age'))

print(user.get('age', 55))
#if age doen't exist then use 55

user2 = dict(name='value')
print(user2)

print('basket' in user)
print('size' in user)

print(user.items()) #prints everything in the dictionary

# print(user.clear()) clears the dictionary
# user2 = user.copy()

print(user.pop('age'))

#user.popitem() randomly pops a pair off the dictionary

print(user.update({'age': 55}))
print(user.get('age'))


#tuple is an immutable list, you cannot modify them

my_tuple = (1,2,3,4,5,5,5,5)
print(my_tuple[1])


print( 5 in my_tuple)

new_tuple = my_tuple[1:2]

print(new_tuple) 

#count method

print(my_tuple.count(5)) #prints the number of 5 in the tuple

print(my_tuple.index(5)) #returns and prints the first index where 5 is found
