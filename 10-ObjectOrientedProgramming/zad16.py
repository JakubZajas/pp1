class Bank_Account:
    def __init__(self,Account_No):
        self.account_no=Account_No
        self.balance=0

    def display(self):
        print("Bank Account NO:",self.account_no)
        print("Balance: ",self.balance," PLN")
    
    def withdraw(self,amount):
        if float(amount)<=self.balance:
            self.balance=self.balance-float(amount)
        else:
            print("Insufficient funds on the account")

    def deposit(self,amoiunt):
        self.balance=self.balance+float(amoiunt)


    
account1=Bank_Account("12 3456 5555 9090 1111 0000 7722")
account1.display()
account1.deposit("25.30")
account1.display()
account1.withdraw("31.70")
account1.display()
account1.withdraw("14")
account1.display()