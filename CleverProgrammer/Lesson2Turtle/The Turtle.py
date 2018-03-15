import turtle

turt = turtle.Turtle() # Creating a class calle turt, this fixes intellisense
#turt.forward(100)
#turt.left(90)
#turt.forward(100)
#turt.right(50)
#turt.forward(100)


#Square

turt.forward(100)
turt.left(90)
turt.forward(100)
turt.left(90)
turt.forward(100)
turt.left(90)
turt.forward(100)

#for loop to make code easier

for steps in range(4):
    turt.forward(100)
    turt.left(90)

