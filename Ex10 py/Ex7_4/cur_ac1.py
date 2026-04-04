from b_ac1 import BankAccount

class CurrentAccount(BankAccount):
    """ A class representing a current (checking) account. """

    def __init__(self, customer, account_number, annualFee, transactionLimit, balance=0):
        """ Initialize the current account. """
        self.annual_fee = annualFee
        self.transaction_limit = transactionLimit
        super().__init__(customer, account_number, balance)

    def withdraw(self , amount):
        """ Withdraw amount if sufficient funds exist in the
        account and amount is less than the single transaction limit."""
        if amount <= 0:
            print('Invalid withdrawal amount:', amount)
            return
        if amount > self.balance:
            print('Insufficient funds')
            return
        if amount > self.transaction_limit:
            print('{0:s}{1:.2f} exceeds the single transaction limit of {0:s}{2:.2f}'.format(self.currency, amount, self.transaction_limit))
            return
        self.balance -= amount

    def apply_annual_fee(self):
        """ Deduct the annual fee from the account balance. """
        self.balance = max(0., self.balance - self.annual_fee)