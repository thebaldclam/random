from b_ac1 import BankAccount
from cur_ac1 import CurrentAccount
from sav_ac1 import SavingsAccount

sav = SavingsAccount("Chan Taiman", 123456, 2)
 
sav.check_balance()
 
print("Deposit 2000.")
sav.deposit(2000)
sav.check_balance()
 
print("Add interest.")
sav.add_interest()
sav.check_balance()
 
print("Check balance under current account.")
cur = CurrentAccount("Alice", 123456, 500, 10000, sav.balance)
cur.check_balance()
 
print("Withdraw 2000 from current account.")
cur.withdraw(2000)
cur.check_balance()
 
print("Apply annual fee.")
cur.apply_annual_fee()
cur.check_balance()
 
print("Deposit 2000 to current account.")
cur.deposit(2000)
 
print("Apply annual fee 500.")
cur.apply_annual_fee()
cur.check_balance()

