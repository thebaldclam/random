from bank_account import BankAccount
from custr import Customer



f = open("12345678.txt", 'w')
f.write("Chan Taiman\n")
f.write("76 Blandings, Sussex\n")
f.write("1976\n")
f.write("1234")
f.close()


while (int(input("Please enter the account number: ")) != 12345678):
    print("Wrong account number, please re-enter!")

f = open("12345678.txt", 'r')
i = 0
list = []
for line in f:
    list.append(str(line))
f.close()

cus1 = Customer(list[0], list[1], int(list[2]))
acc1 = BankAccount(cus1, 12345678, 1000)


while (input("Enter the password: ") != cus1.password):
    print("Wrong password, please re-enter!")

print("You need to change your password")
pw = "a"
npw = "b"

while (npw != pw):
    pw = input("Enter new password: ")
    npw = input("Re-enter the new password: ")
    if pw == npw:
        print("Your new password is " + str(pw))
        cus1.password = pw
        f = open("12345678.txt", 'w')
        f.write(cus1.name)
        f.write(cus1.address)
        f.write(str(cus1.year_of_birth) + '\n')
        f.write(cus1.password)
        f.close()
    else:
        print("Not matching, please enter password again!")
