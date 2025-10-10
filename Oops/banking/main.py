from banking import BankAccount, savingaccount, currentaccount, fixedDeposit
h1= savingaccount(1000,"sumit",10000,12)
h1.computebalance()

h2= fixedDeposit(1001,"sanika",500000,8,2)
h2.computebalance()

h3= currentaccount(1002,"snehal",20000)
h3.withdrawamount(25000)

h4 = BankAccount(1003,"sagar",15000)
h4.get_details()
