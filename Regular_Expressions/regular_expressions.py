#regular expressions

import re

string = 'search inside of this text please'

print('search' in string)

print(re.search('this', string))