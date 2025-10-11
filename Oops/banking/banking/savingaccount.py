from .baseclass import BankAccount 
class savingaccount(BankAccount):
    def  __init__(self,account_number,account_holder,balance, interestrate= 4 ):
        super().__init__(account_number,account_holder,balance)
        self.interestrate=interestrate
    def computebalance(self):
        interest=( self.balance*self.interestrate)/100
        self.balance= self.balance + interest
        print(self.balance )

