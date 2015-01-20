
OriginalBalance=balance
monthlyInterestRate=annualInterestRate/12
MinimumFixedMonthlyPayment=10
while balance>0:
	for i in range(12):
		monthlyUnpaidBalance=balance-MinimumFixedMonthlyPayment
		UpdatedBalance=monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)
		balance=UpdatedBalance
	if balance>0:
		MinimumFixedMonthlyPayment=MinimumFixedMonthlyPayment+10
		balance=OriginalBalance


print 'Lowest payment: ' + str(MinimumFixedMonthlyPayment)
