# how do you write to a file with code?
''' we use the open function to open the file

# myFile = open(filename, accessMode)

##### you must give a file name and access mode
'''
# What is access mode?
'''
This is going to indicate what we can do with it after we open it
###r - read the file
###w - write to file
###a - append existing file content
###b - open a binary file
'''
# use cases: automation, logging for debugging, errors, etc.

#ex

fileName = "demo.txt"
WRITE = 'w' 
APPEND = 'a'
READWRITE = 'w+' #as implied, gives access to both properties

myFile = open(fileName, mode = WRITE) # This actually created demo.txt for us wow!

# How do we write to files? Use the Write function

myFile.write('Hi there! \n') # We have to tell it to put in a brand new line \n
myFile.write('How are you?!')

# what happens if the program crashes and the file locks up?
#   that's why we should close everything we open

myFile.close() # always close something you just used.

print('File written successfully!') # let's create a logging system to confirm 

