from bank_account import BankAccount

my_account = BankAccount("Chan Taiman", 123456, 1000)
print("Hello " + my_account.customer + ",")
print("Account " + str(my_account.account_number) + " has a balance of HKD " + str(my_account.balance))
my_account.deposit(-64)
my_account.deposit(2000)
print("You have deposited " + str(2000) + " balance is " + str(my_account.balance) + ".")
my_account.withdraw(50000)
my_account.withdraw(-64)
my_account.withdraw(1500)
print("You have withdrawn " + str(1500) + " balance is " + str(my_account.balance) + ".")
