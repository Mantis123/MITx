




balance=4213
annualInterestRate=0.2
monthlyPaymentRate=0.04
MonthlyInterestRate=annualInterestRate/12.0

Months=1
unpaidBalance=balance-monthlyPaymentRate*balance
updatedBalance=unpaidBalance+MonthlyInterestRate*unpaidBalance
print 'Month: '+ str(Months) 
print 'Minimum monthly payment: '+ str(round(monthlyPaymentRate*balance,2))
total=monthlyPaymentRate*balance
balance=updatedBalance
print 'Remaining balance: '+str(round(balance,2))
Months+=1
while Months <13:
	unpaidBalance=balance-monthlyPaymentRate*balance
	updatedBalance=unpaidBalance+MonthlyInterestRate*unpaidBalance

	print 'Month: '+ str(Months) 
	print 'Minimum monthly payment: '+ str(round(monthlyPaymentRate*balance,2))
	print 'Remaining balance: '+str(round(updatedBalance,2))
	Months+=1
	total=total+monthlyPaymentRate*balance
	balance=updatedBalance

print 'Total paid: ' + str(round(total,2)) 
print 'Remaining balance: ' + str(round(balance,2))



