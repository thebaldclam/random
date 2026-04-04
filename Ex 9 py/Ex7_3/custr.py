class Customer:
    """ A class representing a bank customer. """
    def __init__(self, nm, addr, y_o_b):
        self.name = nm
        self.address = addr
        self.year_of_birth = y_o_b
        self.password = "1234"
        
    def get_ad(self):
        return self.address
    
    def get_age(self):
        """ Calculates and returns the customer"s age. """
        thisYear=2025
        return thisYear - self.year_of_birth