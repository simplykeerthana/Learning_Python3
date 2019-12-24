# strings

print("Keerthana Madhavan")

print(type("Keerthana Madhavan")) # class <'str'>

# strings can either be in double quotes or single quotes
userrname = 'supercode'

password = 'supersecret' 

#third way to write strings in python ' ' ' multiple statemetns ' ' '
#multiple line strings

long_string = '''
WOW
O O
___

'''

print(long_string)



# strings using variables

first_name = 'Keerthana'
last_name = 'Madhavan'

full_name = first_name + last_name

print(full_name)

#string concatenation , adding strings together


print('hello' + ' world')

print(str(100))

#type conversions .

print(type(int(str(100))))

#the above line can be written as 

a = str(100)
b = int(a)
c = type(b)
print(c)

#escape sequences \ is used for escape sewuences

weather = "It\'s \"kind of  cold\" \n hope you have a good day"

print(weather)

#when in doubt just go to python documentation. 

#formatted strings, a new feautre of Python3
# add f in front of the beginning of the string
name = 'Johnny'
age = "46"
print('hi' + name + '. You are' + str(age) + 'years old')

print("Formatted string version")

print(f'hi {name}. You are {age} years old')


