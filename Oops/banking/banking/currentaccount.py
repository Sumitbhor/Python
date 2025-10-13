from .baseclass import BankAccount

class currentaccount(BankAccount):

    def __init__(self, account_number, account_holder, balance,overdraft_limit=100):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdrawamount(self,amount):

        self.balance= self.balance + self.overdraft_limit
        if amount>self.balance:
            print("withdrawing amount more than balance ")
            print("Current balance:", self.balance)
        else:
            super().withdraw(amount)

    def deposit(self, amount):
        return super().deposit(amount)
    
    def getdetails(self):
        return super().get_details()
    
