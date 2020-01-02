#generators in python
# allows us to generate a sequence of values overtime, for ex range is a generator

range(100) #creates 1 by 1
list(range(100)) # creates and stores 100 elements in memory


#creating a list instead of using a list function
# this list is created in memory
def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)

 #use a generator to access large number of elements in a list, one at a time
#everything that is a generator is iterable, generator is a subset of a iterable

# whereas this list created already and we use it one by one. 
def generator_function(num):
    for i in range(num):
        yield i #give the element 1 by 1 
    
for item in generator_function(1000):
   print(item) 


#testing time for non range and range functions

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1}")
        return result
    return wrapper

@performance 
def long_time():
    print('range')
    for i in range(10000000):
        i*5

@performance
def long_time1():
    print('non-range')
    for i in list(range(10000000)):
        i*5


long_time()
long_time1()


# another generator example: for loop and RANGE


#for loop
# all the iterations are in the same memory space
def special_for(iterable):
        iterator = iter(iterable)
        while True:
            try:
                print(iterator)
                print(next(iterator))
            except StopIteration:
                break

special_for([1,2,3])

#RANGE functions

class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __iter__(self):
        return self
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current +=1
            return num
        raise StopIteration


gen = MyGen(0,100)

for i in gen:
    print(i)
