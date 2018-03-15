#math operations!

#Exponents are ** ex below
# 5**2 = 25

#Modulo ex below (%)
# example 5 divided by 43 has a remainder of 3
# scenario
#    programming trick to detect frequency of something.

moduloTest = 5%43
print(moduloTest) #Prints 5?? Why?

#ORDER OF OPERATIONS STILL MATTER :D

print("\n")

area = 0 #initializing
height = 10
width = 20

#calc area of a triangle
area = width * height /2

# print("The area of the triangle would be " + area)
# ^^ area is a number, cant concatanate string to the area

# %d = decimal number, %f is a float number.
#   Example below is the only way to concatenate string + numbers
print("The area of the triangle would be %.2f " % area) #.2f specifies ONLY 2 decimals after the final calc


# 32 spaces between the string and the number
print("My favorite number is %32d !" % 42)

# formatting decimal number with right justified to take up 6 spaces with leading zeroes 
print("My favorite number is %06d !" % 42)

print("My favorite number is %3d !" % 42)

# This syntax is more consistent with other programming languages
#   {0:d} this is the position of the number.
#   {1:d} is the next number 
print("I have {0:d} cats".format(6))

#ex
print("the area of the triangle would be {0:f} ".format(area))
print("my fav numb is {0:d} ".format(42))

print("Here are three numbers! The first is {0:d} The second is {1:4d} and {2:d} ".format(7,8,9))

# you can use \ to continue command on next line

total = 5 + 6 + 5 + 5 + 6 + 6 \
    + 999 + 55050505050 
print("This is a continued command on next line %d " % total)

