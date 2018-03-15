#Scenario of lists
''' remember everyone coming to a party 
scores in all your courses
directions to your doctors appointment

'''

# Declaring a list

guests = ['Chris','Susan','Bill','Satya']

#scores = [50000,2592] 

# You can create an empty list and add values later

butts = [] # This is an empy list!
scores = []

# How do we ask for a specific value though?
print(guests[0]) # We're calling an index position
#print(scores[1])

print(guests[-1]) #This prints Satya

print(guests[-4]) # This prints chris

#Update values in a list

print('first value is ' + guests[0])

#change value
guests[0] = 'Steve'
print('first value is now ' + guests[0])

#Append Func.

''' this adds only at the end of the list '''

guests.append('Billy') 

print(guests[-1])

guests.remove('Satya')

print(guests)

#works just like guests.remove, but with list number
del guests[0] #Doesnt use a guests.del, weird off one syntax

print(guests)

#Update a value directly in a list
guests[2] = 'Jessica'
print(guests)


#Index()
''' function will search the list and return 
the index of the position where the value was found 
'''

guests.append('Ted')
print(guests)
print(guests.index('Ted')) # will print position in the list

'''SCENARIOS
A. There are multiple bills in the list, how can we remove them all bills at once?
B. There are thousands of people with names that start with D, 
how do we remove them all? (Loops?)
    2B. (We could use string tricks to target names in a list that 
    start with D first, then remove, in a loop)
'''

#Using a For Loop to print length of the list

for steps in range(4): # This prints all names in a list
    print(guests[steps])

guests.append('Dave')
guests.append('MADAMADA')
guests.append('Genji')
guests.append('Hanzo')
guests.append('Zeus')
guests.append('Hashi')

#for steps in range(4): ##### Using a while loop to help us list out unknown number of list items??
#    print(guests[steps])

#print(guests.count)) 
''' do not use .count to count multiple items, bad for perf.  Counter is the good alternative'''


###### How to print all lists of names until the end of the list is hit!!
#listCounter = 0
#while listCounter<len(guests):
#    print(guests[listCounter])
#    listCounter = listCounter + 1


##### Exactly the same as NBRENTRIES and the for loop below, but embedded len in the range!!
#for listCounter2 in range(len(guests)):
#    print(guests[listCounter2])

''' len() to find out how many entries are in your list '''

nbrEntries = len(guests)

#Course loop that executes one for each entry
### Similar to loop above from outside the course

for steps in range(nbrEntries):
    print(guests[steps])
    ''' but how do I list a number of list entries?? Index()??? '''


##### Even easier way to go through all items in a list
currentGuestTracker = 0
print(guests)
for currentGuest in guests : # For every count in guests, add to listItem, aka finished until done :O
    print(currentGuest)
    currentGuestTracker = currentGuestTracker + 1
    print(currentGuestTracker) # works, but probably a laggy approach in sorting data


### Sort Method.
# Perfect for sorting names in alphabetical order

guests.sort()

# Let's print the list

print(' Oh wow this is an alphabetically sorted list! ')
for guest in guests :
    print(guest)
