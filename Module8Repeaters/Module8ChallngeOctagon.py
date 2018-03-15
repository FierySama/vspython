import turtle

myTurtle = turtle.Turtle()

#Force user to input the amount of sides, #bonus 1
nbrSides = input('Please enter the amount of sides an object will have... ')

#Data convert a str into int early, Is there a more clean version to do this?
nbrSides = int(nbrSides)

for sides in range(nbrSides):
    myTurtle.forward(100)
    myTurtle.right(360/nbrSides)
    for inside in range(nbrSides):
        myTurtle.forward(100)
        myTurtle.right(360/nbrSides)
# how do i get the code to draw a smaller version of the same shape inside? Stamping maybe

myTurtle.color(red)
myTurtle.stamp