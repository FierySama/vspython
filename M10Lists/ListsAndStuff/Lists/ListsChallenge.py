''' # Objective: Let's ask someone who they want to invite, we don't know how many guests are coming,
    # and stop should end user input

1) Ask user to enter the names of everyone attending a party -- DONE
2) Return list in alphabetical order -- DONE
2) while loop for the unknown amount of people -- DONE
    2b) how do we make STOP finish in the loop? -- DONE
        I) We use an if statement to filter against stop -- CAN BE USED, MORE EFFICIENT
        II) Or we can use another loop to remove stop -- DONE
       on repeat from list before print. (VERY SLOW for efficiency, but works)
'''
#Initializers
attendees = []
name = "   "
nbrAttendees = len(attendees)

# Let's ask the user for names of all people attending the party
while name != 'DONE' :
    name = input('Who is attending? (Enter DONE when finished) \n').upper()
    attendees.append(name) # this might have been the key thing missing, i wasn't adding anything to the list
    nbrAttendees = nbrAttendees + 1 # counter to keep track of names
    print('Number of Attendees {}'.format(nbrAttendees) ) # {} allows for .format to insert the nbrattendees
    
    ''' 
    #if 'DONE' in attendees :
    #    attendees.remove('DONE') # Also works!
    # OR we could use
    # if attendees.upper() != 'DONE' :
        #attendees.append(name)
    '''

''' Below, we are trying to delete all of stop with another while loop'''

while 'DONE' in attendees : attendees.remove('DONE') # IT WORKS!!!!!!!!

    
print('Enjoy the party, and enjoy the succ ')

# sort then return list in alphabetical order
''' .sort works for this '''

attendees.sort() # Yay alpahbetical now

for insertednames in attendees: 
    print(insertednames)