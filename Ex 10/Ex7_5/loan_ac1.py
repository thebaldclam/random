from b_ac1 import BankAccount

class LoanAccount(BankAccount):

    def __init__(self, customer, account_number, loan_interest_rate, balance=0, loan=0):
        self.loan_interest_rate = loan_interest_rate
        self.loan = loan
        super().__init__(customer, account_number, balance)

    def setLoan(self, amount):
        if amount > 0:
            self.loan += amount
            print("A loan of {:s} {:.2f} is set up.".format(self.currency, amount))
            print("The current loan is {:s} {:.2f}.".format(self.currency, self.loan))
        else:
            print("Invalid loan amount of {:s}{:d}.".format(self.currency, amount))

    def retLoan(self, amount):
        if amount <= 0:
            print("Invalid return-loan amount of {:s}{:d}.".format(self.currency, amount))
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.loan -= amount
            self.balance -= amount
            print("A loan of {:s}{:.2f} is returned.".format(self.currency, amount))
            print("The current loan is {:s} {:.2f}.".format(self.currency, self.loan))

    def debit_interest(self):
        interest = self.loan * self.loan_interest_rate / 100
        self.balance -= interest
