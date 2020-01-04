#password checker project

# secure way to check if your password has ever been hacked

# have you been pwned api is good for password checker

# build your own password checker and secure API

import requests
import hashlib

#this API uses hasing, make the passwoed gibberish. use an hasing generator - https://passwordsgenerator.net/sha1-hash-generator/
# you just need 5 characters of the hasg



#print(res) #response 400 is not good, usually means unauthorized, 200 means ok

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def pwned_api_check(password):
    #check password if it exists in API response
    print(password.encode('utf-8'))
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #to encode the password
    #sha1password = hashlib.sha1(password.encode('utf-8'))
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail)
    print(response)
    return response
#request_api_data(123)


pwned_api_check('123')

