class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def debit(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"{amount} is debited,balance is {self.getbal()}")
        else:
            print("insufficient funds")
    def credit(self,amount):
        self.balance+=amount
        print(f"{amount} is credited,balance is {self.getbal()}")
    def getbal(self):         #this lines are not needed instead use self.balance in place of
        return self.balance    #self.getbal()
'''acc1=Account(1000,"acc123")
acc1.credit(200)
acc1.debit(1200)'''
class Savingsaccount(Account):
    def __init__(self,interest):
        self.interest=interest
        super(). __init__(1000,"acc123")
    def interestrate(self):
        interest1=self.balance*(self.interest/100)
        self.balance+=interest1
        print(self.getbal())
acc1=Savingsaccount(5)
acc1.credit(200)
acc1.debit(200)
acc1.interestrate()

