# fibonnacci sequecne using an generator
#interview sequence

# first num = 0
# seconf num = 1


def fib(number): #number = index number
    a = 0
    b = 1
    for i in range(number):
        yield a 
        temp = a
        a = b
        b = temp + b
         
for x in fib(25):
    print(x)

#print(fib(25))


#in a list 

def fib2(number): #number = index number
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b 
    return result

print(fib2(10))
