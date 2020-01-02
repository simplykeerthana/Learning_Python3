#generators in python
# allows us to generate a sequence of values overtime, for ex range is a generator

range(100) #creates 1 by 1
list(range(100)) # creates and stores 100 elements in memory


#creating a list instead of using a list function
def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)

 #use a generator to access large number of elements in a list, one at a time
#everything that is a generator is iterable, generator is a subset of a iterable

def generator_function(num):
    for i in range(10000000):
        yield i #give the element 1 by 1
    
for item in generator_function(1000):
    print(item)