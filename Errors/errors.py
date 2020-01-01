# errors and error handling in Python
#an error that crashes programs are exceptions. 


#print(1+True)

while True: #try until an integer is entered
    try:
        age = int(input("what is your age? "))
        # 10/age
        #raise ValueError('hey cutt it out')
        print(age)
    except ValueError: #handling the error from above input, if the user enters non integer
        print('please enter a number')
    except ZeroDivisionError: #handling the error from above input, if the user enters non integer
        print('please enter age higher than 0')
    else: 
        print('thank you!')
        break
    finally: #runs regardless of anything
        print("ok, i am finally done")

print()
print()

def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err: 
        print(f"Please enter numbers {err}" )

print(sum(1, '2'))