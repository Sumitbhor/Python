class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print( self.balance)
        print("Invalid deposit amount")
    def withdraw(self,amount ):
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance-=amount
            print(self.balance)
    def get_details(self):
        print (
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.account_holder}\n"
            f"Balance: {self.balance}"
        )

