class BAc2:
    """ A base class representing a bank account."""
    currency = 'HKD'

    def __init__(self, customer, account_number, balance = 0, loan = 0):
        "Initialize the BankAccount class with a customer, account number and opening balance (which defaults to 0.)"
        self.customer = customer
        self.account_number = account_number
        self.balance = balance
        self.loan = loan 

    def deposit(self, amount):
        """ Deposit amount into the bank account."""
        if amount > 0:
            self.balance += amount
        else:
            print('Invalid deposit amount: ', amount)
    
    def withdraw(self, amount):
        """Withdraw amount from the bank account, ensuring
        there are sufficient funds."""
        if amount > 0:
            if amount > self.balance:
                print('Insufficient funds')
            else:
                self.balance -= amount
        else:
            print('Invalid withdrawal amount: ', amount)

    def check_balance(self):
        """ Print a statement of the account balance. """
        print('The balance of account number {:d} is {:s}{:.2f}'.format(self.account_number, self.currency, self.balance))

    def setLoan(self, amount):
        if amount > 0:
            self.loan += amount
            print('A loan of {:s} {:.2f} is set up.'.format(self.currency, amount))
        else:
            print('Invalid loan amount of {:s}{:d}'.format(self.currency, amount))



    
