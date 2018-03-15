#step 1 initialize, step 2 ask for user input in string format, step3 convert from string to float/int/?
#step 4 put it all in the calcultion

#NOTE: How can you convert strings and do the calculation at the same time??

# Loan Calculator

#interestrate
i = 0.05


#n = numberofpayments
#L = loanAmount
L = 0
#M = monthlypayment
monthlyPayment = 0
#M = L*[i(1+i)n] / [(1+i)n-1]

L = input("What is your total Loan amount? ")
n = input("How many payments do you have left? ")

# 
monthlyPayment = float(L)*[i*(1+i)*float(n)] / [(1+i)*float(n)-1]

print(monthlyPayment) 