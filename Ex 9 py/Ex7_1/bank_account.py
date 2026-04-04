class BankAccount:
    """ A base class representing a bank account."""
    currency = "HKD"

    def __init__(self, customer, account_number, balance=0):
        "Initialize the BankAccount class with a customer, account number and opening balance (which defaults to 0.)"
        self.customer = customer
        self.account_number = account_number
        self.balance = balance 

    def deposit(self, amount):
        """ Deposit amount into the bank account."""
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount: ", amount)
    
    def withdraw(self, amount):
        """Withdraw amount from the bank account, ensuring
        there are sufficient funds."""
        if amount > 0:
            if amount > self.balance:
                print("Insufficient funds")
            else:
                self.balance -= amount
        else:
            print("Invalid withdrawal amount: ", amount)



    
