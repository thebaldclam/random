from bank_account import BankAccount
from custr import Customer


cus1=Customer('Chan Taiman', '76 Blandings, Sussex', 1976)
acc1=BankAccount(cus1, 12345678, 1000)
print("Customer's age is {}.".format(acc1.getCus().get_age()))
print("Customer's address is {}.".format(acc1.getCus().get_ad()))
f = open(str(acc1.account_number)+'.txt', 'w')
f.write(cus1.name + '\n')
f.write(cus1.address + '\n')
f.write(str(cus1.year_of_birth) + '\n')
f.write('1234')

while (int(input("Please enter the account number: ")) != acc1.account_number):
    print('Wrong account number, please re-enter!')

while (input("Enter the password: ") != cus1.password):
    print('Wrong password, please re-enter!')

print('You need to change your password')
pw = 'a'
npw = 'b'

while (npw != pw):
    pw = input('Enter new password: ')
    npw = input('Re-enter the new password: ')
    if pw == npw:
        print('Your new password is ' + str(pw))
        cus1.password = pw
        f.write(cus1.name + '\n')
        f.write(cus1.address + '\n')
        f.write(str(cus1.year_of_birth) + '\n')
        f.write(pw)
    else:
        print('Not matching, please enter password again!')

f.close()