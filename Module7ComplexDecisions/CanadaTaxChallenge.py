# remember to initialize values
# remember to ask for input in lower or upper
# remember to get the and logic right if used, and use parantheses everywhere
# check list
''' TO DO
1. ask if from canada -- DONE
2. ask which province -- DONE
3. if not canada, charge no taxes -- DONE
4. if order was placed in Canada, calculate tax based on province.. -- TODO
	4a. find a lazy way to deal with other province charge! :D -- TODO
5. Do the calculation of selected provinceTax and the price of their purchase -- TODO

'''

''' Mistakes made

1. Don't *really* need booleans for this program, but would make it easier as a persistent
feature for the base back end of the 'site' I feel.
2. I didn't declare separate tax rates for each province. This leads to non - modular code,
which makes it much much harder to maintain for other devs.
    2a. provinceTax makes it easy for writing code, but will screw over a site that needs 
    their taxes updated instantly.

'''

#initializing booleans and values
fromCanada = False 
outsideCanada = False
province = ''
fromWhere = ''
provinceTax = 0
orderAmount = 10 # Let's just assume it's $10 cad minimum to shop here
#ask if from canada, then ask which province

fromCanada = input('Where do you live? ').lower()


if fromWhere == 'canada':
	fromCanada = True
	print('Awesome, which province do you live in? ')
	print('Alberta, Ontario, New Brunswick, Nova Scotia, or other? ')
	province = input('').lower()
elif fromWhere != 'canada':
	print("You don't seem to be from Canada, enjoy your no taxes! ")


if province == 'alberta':
	provinceTax = .05
	print('You will be charged 5% taxes' )
elif province == 'ontario' or province == 'new brunswick' \
    or province == 'nova scotia':
    print('Sorry, your tax rate is 13%! ')
    provinceTax = .13
else: 
    print('Hey! You\'re not in any of those provinces in canada,\
    so you\'ll have to pay 6 % plus GST of 5% ')
    provinceTax = .11
    print('The tax rate is: %1f' % provinceTax)
        #fuckkkk, why does this part keep showing if you dont put canada??

 # how do I do the maths?