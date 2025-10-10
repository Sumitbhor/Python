from .baseclass import BankAccount 
class currentaccout(BankAccount):
    def __init__(self, account_number, account_holder, balance,overdraft_limit=100):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdrawamount(self,amount):
        if amount>self.balance:
            self.balance= self.balance + self.overdraft_limit
            print("withdrawing amount more than balance so overdraft is used")
            self.balance -= amount
            print("Current balance:", self.balance)
        else:
            print("withdrawing amount from current account")
            self.balance -= amount
            print("Current balance:", self.balance)
