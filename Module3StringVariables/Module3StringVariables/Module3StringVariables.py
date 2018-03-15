#String variables, and asking users to input a value
print("What is your name? ")    # This allows for the next line to be user input
name = input("")

country = input("What country do you live in? ")
country = country.upper()
print(country)

# input is command to ask user to enter info!!
# name is actually the name of a custom variable that we've created above.

#Create a friendly output

print("Hello! " + name + ", please create your story! ")
print("\n")
#Variables allow you to manipulate contents of VARIABLES

message1 = "Hello World \n"
print(message1.lower()) #hello world
print(message1.upper()) #HELLO WORLD
print(message1.swapcase()) #hELLO wORLD


#Update value of name after user input

# name = "banana hammock"
#print(name)

# Variables are case sensitive!!! Name does NOT EQUAL name
#       Treat everything like it's case sensitive in python.
#       Variables cannot start with a number.
#           name3 name2 name1 are all okay


# Newer functions!!
print("\n")
message2 = "hello World"
print(message2.find("world"))
print(message2.count("o"))
print(message2.capitalize())
print(message2.replace("Hello","Hi"))

#Good habit. Initializing values 
#ex below

postalCode = " " #this is declaring that this is a string, with initializing
postalCode = input("Please enter your postal code: ")
print(postalCode.upper())