from .baseclass import BankAccount

class fixedDeposit(BankAccount):

    def __init__(self, account_number, account_holder, balance,interestRate=4, time=1):
        super().__init__(account_number, account_holder, balance)
        self.interestRate= interestRate
        self.time= time

    def computebalance(self):
        interest= (self.balance*self.time*self.interestRate)/100
        self.balance += interest
        print(self.balance)