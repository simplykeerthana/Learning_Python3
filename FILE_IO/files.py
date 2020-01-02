#file IO 
#input something from the outside world and output something to the outside world

#input a pdf file 
#output a pdf file
 
#open file 

my_file = open('test.txt')

print(my_file.read())  #you can only read the files once, becayse the cursor goes to eof

my_file.seek(0) #to point to the beginning of the file

print(my_file.read())

my_file.seek(0)
print(my_file.readlines)


#you haave to close the files after you open it

my_file.close()

#read, write, append

#r+ read write
# 'a' hey it appends to the end of the file

with open('test.txt', mode='a') as my_file1:
    text = my_file1.write(' hey it is me')
    print(text)
    #print(my_file1.readlines())

my_file1.close()

#if we don't specify the mode, then it is automatically read

# with open('test.txt', mode='r') as my_file

#write to a file

#creating a file that does not exist

#with open('sad.txt', mode='w') as my_file2:
 #   text = my_file2.write(':(')


#file paths


# path lib module - explore

#File IO Errors

try:
    with open('sad.txt', mode='r') as my_file3:
        print(my_file3.read())
except FileNotFoundError as err:
    print('file does not exist ')
    raise err
except IOError as err:
    print('IO error')
    raise err