# list,  set, dictionary.... can be used with comprehensions
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100)]

my_list4 = [num**2 for num in range(0,100) if num % 2 ==0 ]


print(my_list4)
#sets - you get pretty much the same answers as list

my_list = {char for char in 'hello'}
my_list2 = {num for num in range(0,100)}
my_list3 = {num**2 for num in range(0,100)}

my_list4 = {num**2 for num in range(0,100) if num % 2 ==0 }

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

#dictionary

simple_dict = {
    'a':1,
    'b': 2
}
my_dict = {key:value**2 for key, value in simple_dict.items()}

my_dict1 = {num: num*2 for num in [1,2,3]}

print()
print()
print(my_dict)
print(my_dict1)

#exercise comprehension
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

#using comprehension

duplicates1 = []

duplicates1 = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates1)