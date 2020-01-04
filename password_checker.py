#password checker project

# secure way to check if your password has ever been hacked

# have you been pwned api is good for password checker

# build your own password checker and secure API

import requests

url = 'https://api.pwnedpasswords.com/range/' + '_password123'
res = requests.get(url)