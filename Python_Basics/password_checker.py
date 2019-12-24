# this mini exercise is a password checker.


username= input('What is username? ')
password = input('What is your password')

passwordLength = len(password)

encrypt_password = ('*' * passwordLength)

print(f'{username} your password {encrypt_password} is {passwordLength} letters long')