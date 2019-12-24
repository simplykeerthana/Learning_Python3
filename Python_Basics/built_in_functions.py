#using string python methods

sample = len('helloooo')

print(sample)

#python string methods


quote = 'to be or not to be'


print(quote.find('be')) # does be exist in the quote string. 

print(quote.replace('be', 'me'))

print("new quote " + quote)

quote2 = quote.replace('be', 'see')

print("new quote 1 " + quote2)


#boolean

name = 'Keerthana'
is_cool = False 
is_cool = True

print(bool(1)) #value is true

print(bool(0)) #value is false 

print("Using true of false through boplean function")
print(bool('true'))
print(bool('false'))

#type conversions 

name = 'Jeremy Irons'
age =  34

relationship_status = 'single'
print(relationship_status)



relationship_status = 'It\'s complicated' 
print('updated version of relationship ' + relationship_status)

birth_year = input('what year where you born') #this takes in a string input so you have to convert to int

your_age = 2020 - int(birth_year)

print(f'Your are age based on your birth year is {your_age}')


