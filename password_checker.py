#password checker project

# secure way to check if your password has ever been hacked

# have you been pwned api is good for password checker

# build your own password checker and secure API

import requests

#this API uses hasing, make the passwoed gibberish. use an hasing generator - https://passwordsgenerator.net/sha1-hash-generator/

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)

print(res) #response 400 is not good, usually means unauthorized, 200 means ok

