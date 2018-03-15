#Dates and Times

#import datetime -- class.
#   A library to work with dates
#import locale -- class.
#   a library to work with currencies

import datetime
currentDate = datetime.date.today() # Must define what currentDate is, and that's with the library datetime

#Within intellisense to complete .today, a purple clear box means () is needed. 
# BLUE BOX means it's a property

print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

##We use strftime to specify date format (String From Time)
##Example

print(currentDate.strftime('%d %b, %Y'))# %b is the month
print(currentDate.strftime('%d %b, %y'))
print(currentDate.strftime('%d %B, %Y'))
#%m is for minutes, so they cant use %m for months
#strftime.org for more syntax

#"Please attend our event X, Y Z in the year y"
print(currentDate.strftime 
      ('Please attend our event %A, %B %d in the year %Y'))

#Localizing date and currency in python. . .
#babel.pocoo.org

######
# CALCULATE DAYS UNTIL YOUR BIRTHDAY, VIA USER INPUT

userInput = input("Please enter your birthday (mm/dd/yyyy) ") #Always returns a string, so we'll convert with strptime

birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
print(birthday)

#STRPTIME func allows you to convert a string to a date

#Creating a countdown until an event

days = birthday - currentDate
print("Days until birthday")
print(days)

