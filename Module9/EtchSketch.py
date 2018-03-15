import turtle

# turt = turtle.Turtle() This is assigning the module of turtle to turt, so intellisense can complete

# Initialize shit

penColor = "black"
lineLength = 1
userAngle = 1

# penColor = input('What\'s your desired pen color? (red, green, blue, black) \t \n')
# lineLength = int(input('How long do you want the stroke to be? Enter 0 to end sketching \t \n'))
# userAngle = int(input('Enter your angle in [0 - 360] to draw at. \t \n '))

while lineLength != 0:
    turtle.color(penColor)
    turtle.right(userAngle)
    turtle.forward(int(lineLength))

    lineLength = int(input('How long do you want the stroke to be? Enter 0 to end sketching \t \n'))

    # This if statement is for repeating questions
    if lineLength != 0:  # This if statement must be nested inside the while loop.

        penColor = input('What\'s your desired pen color? (red, green, blue, black) \t \n')
        userAngle = int(input('Enter your angle in [0 - 360] to draw at.\t \n '))

print("You are an amazing artist!")
