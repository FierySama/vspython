#Reading from files in python
'''
Potential use cases

reading a shopping list at the grocery store

phone books

ebook reader knows what page you were on, what chapter.

video games that know where you left off of.

Reading and processing OpenData
    imagine using open data to create an app to make a useful app,
    like recent health inspections happening for a restaurant
        We can do that with python! What!?

Web scraping

'''

#Declare constants for accessMode
''' What's the point of these?
Constants are a way of telling other programmers to leave them unchanged, as they represent something
that shouldn't be changed to keep the code easily maintained.

'''

WRITE = 'w' 
APPEND = 'a'
READWRITE = 'w+' #as implied, gives access to both properties
READ = "r"

#defining fileContent to reading myFile

#############fileContent = myFile.read() # Returns EVERYthing from the file, dumps into a single string.


#Open file command,

animalFile = open(fileName, mode = READ)
fileContent = myFile.read()
print(fileContent)
animalFile.close()
