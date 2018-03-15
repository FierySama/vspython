# Let's make a csv type of file thing

fileName = "Names.csv"
WRITE = 'w' 
APPEND = 'a'
READWRITE = 'w+' #as implied, gives access to both properties

data = input('Please enter file info')
file = open(fileName, mode = WRITE)
file.write(data)
file.close()

######myFile = open(fileName, mode = READWRITE) #creates and sets permission to file

# How do we write to files? Use the Write function

########myFile.write('Julia Anderson, 26\n') # \n
########myFile.write('Billy Bobby, 23\n')
########myFile.write('Dominic butts, 86\n')
########myFile.write('Billy bob, 69\n')

##myFile.close() # always close something you just used.

print('File written successfully!')
