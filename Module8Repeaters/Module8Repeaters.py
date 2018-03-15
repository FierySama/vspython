## Repeaters
# Using loops to draw! :O 

import turtle

##Perfect situation for using a loop
#turtle.forward(100)
#turtle.right(90)
#turtle.color('red')
#turtle.forward(100)

#For Loops!
'''
Yay!
'''

##steps is a variable name we made
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)


#Nested Loops
''' Someone help me ;( '''

nbrSides = 5
for steps in range(nbrSides):
    print(steps)
    turtle.forward(100)
    turtle.right(360/nbrSides)
    for moresteps in range(nbrSides):
        turtle.forward(50)
        turtle.right(360/nbrSides)
# Makes a star with hexagons :O 

# HOW TO COUNT STARTING FROM 1????
''' for steps in range(1,4):
    print(steps)
'''
print('spacer')
for steps in range(1,4): # This would execute only 3 times, counts to 3, NOT 4
    print(steps)
print('spacer')
for steps in range(1,10,2): # This is a skip step, "jump  by 2 " in this case
    print(steps)
print('spacer')
for steps in [1,2,3,4,5]: # NOTE: Range is gone, and BRACKETS instead of paran.
    print(steps)
#We're telling this for loop ^ to use exactly those values in the [] args
''' we also dont need to use numbers at all for the above '''

#Example:

for steps in ['red','blue','green','black']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)

