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

