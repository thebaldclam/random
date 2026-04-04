from loan_ac1 import LoanAccount

acc = LoanAccount("Chan Taiman", 123456, 5, balance=1000)

print("Hello {:s},".format(acc.getCus()))
acc.check_balance()
acc.setLoan(2000)
acc.retLoan(500)
acc.check_balance()
acc.debit_interest()
acc.check_balance()
