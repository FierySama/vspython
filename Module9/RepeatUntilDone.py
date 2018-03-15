#looping until code executes
''' potentially from one to the next, over and over, for an UNKNOWN amount of times 

looping files, looping database tables (someone from a specific country ex), 
'''

#AKA WHILE LOOPS!!!!

answer = '0' #While loop needs initalization in advance 
''' why a string?

Math question is irrelevant, an input gives back a string.'''

while answer != "4":
    answer = input("What is 2 + 2?\t ")
    # how could we tell it to try again if it's still not 4?

print("Yes 2 + 2 = 4") # This will only print if the while loop ends

