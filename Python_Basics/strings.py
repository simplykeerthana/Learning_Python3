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

#variable fill in using brackets
print('hi {}. You are {} Years Old'.format('Jhonny', '55'))
print('hi {}, You are {} Year Old'.format(name, age))


#indexed Strtings

selfish =  'me me me' 
# 0-m, 1-2,  acessing different parts of the string using indexes

print(selfish)
print(selfish[1])
print(selfish[0])

#[start: stop] you can start from start and where to start

sample = '01234567'
print("Start:Stop indexes using strings")
print(sample[0:2]) # so start at 2 and as soon as you get to book shelf 2 that is value '2' you stop
print(sample[0:7])

print(sample[-1] # in python the negative index sarts at the end of string)

#[start:stop:stepover], slicing the string

print(sample[::-1]) # prints the reverse of the string

#immutability - strings in python are immutable
# you can only completely reassign the variable of the string. 

sample = sample + '8' #this just appends 8 to the sample

print(sample)