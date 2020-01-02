#useful module in python

#collection moudle 

from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
print(Counter(li))  #counte create a ditionary, how many times an item occured in a iterable

sentence = 'blah blah blah thinking about coop job' #counts repetition of each character

print(Counter(sentence))

#default dict

dictionary = defaultdict(lambda: "Does not exist",{'a':1, 'b':2})
print(dictionary['c'])

#Ordered Dict, retains the order that you insert into the dictionary

d = OrderedDict()
d['a'] =1
d['b'] =2

d2 = OrderedDict()
d2['a'] =1
d2['b'] =2

print(d2 == d) #gives true

#datetime module

import datetime

print(datetime.time(5,45,2))
print(datetime.date.today())

from array import array

#lists are dynamic
#arrays take up less memory and take less space

arr = array('i', [1,2,3])
print(arr[0])


