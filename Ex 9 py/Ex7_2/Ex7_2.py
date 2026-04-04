from b_ac2 import BAc2

acc = BAc2("Chan Taiman", 123456, 1000)
print("Hello " + acc.customer + ",")
print("Account " + str(acc.account_number) + " has a balance of HKD " + str(acc.balance))
acc.setLoan(-64)
acc.setLoan(0)
acc.setLoan(2000)
acc.setLoan(3000)
acc.retLoan(0)
acc.retLoan(5000)
acc.retLoan(500)
acc.retLoan(100)
acc.check_balance()
