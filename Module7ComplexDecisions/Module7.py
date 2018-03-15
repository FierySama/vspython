# elif allows us to check for diff values
# elif means else if
  
country = input("Where are you from? ").upper()

# Always test conditions and all cases possible

if country == "CANADA":
    print("Hello ")
elif country == "GERMANY":
    print("Guten Tag! ")
elif country == "FRANCE":
    print("Bonjour ")
else:
    print("Please try a different country ")

# for some reason .upper is not working?? -----> Fixed by added .upper() at end of input
