#regular expressions

import re

string = 'search inside of this text please'

print('search' in string)

a = re.search('this', string)

print(a.span())
print(a.start())
print(a.group())
print(a.end()) 

pattern = re.compile('search this inside the fucntion')

a1 = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(c)

#relearn regex again
