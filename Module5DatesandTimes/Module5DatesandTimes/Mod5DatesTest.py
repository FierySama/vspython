import datetime
currentDate = datetime.date.today()

print(currentDate.strftime 
      ('Please attend our event %A, %B %d in the %Y'))

userInput = input("Please enter your birthday (mm/dd/yyyy) ") #Always returns a string, so we'll convert with strptime

birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
print(birthday)

days = birthday - currentDate
print("Days until birthday")
print(days)

