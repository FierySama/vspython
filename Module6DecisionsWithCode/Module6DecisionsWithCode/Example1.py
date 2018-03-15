# meanwhile, earlier in the day
bestTeam = "senators"

# #### If statements with string
# favoriteTeam = input("What is your favorite hockey team? ")
# if favoriteTeam.upper() == bestTeam.upper()  :
#    print("Yeah, go sens go! ")
# print("If it's okay if you prefer football/soccer )  ")


# if with numbers
freeToaster = False  # Initializing the boolean before user input

deposit = int(input("how much do you want to deposit? "))
if deposit > 100:  # boundary condition : IS MANDATORY for if and else
    # Boolean with freeToaster
    freeToaster = True


# pretend complex code here....

if freeToaster:  # This means that if freeToaster is true, it will display if freeToaster==True : works too!
    print("Enjoy your toaster! ")

else:
    print("Enjoy your Mug!")

print("Have a nice day! ")
