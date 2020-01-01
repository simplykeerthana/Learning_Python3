# errors and error handling in Python
#an error that crashes programs are exceptions. 


print(1+True)

try:
    age = int(input("what is your age"))
    print(age)
except:
    print('please enter a number')