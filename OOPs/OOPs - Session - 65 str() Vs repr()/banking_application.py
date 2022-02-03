class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if self.balance>=self.min_balance:
            self.balance=self.balance-amount

        else:
            print('Insufficient funds')

    def print_statement(self):
        print('Account Balance:',self.balance)

class CurrentAccount(Account):

    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)

    def __str__(self):
        return "{}'s current account balance is:{}".format(self.name,self.balance)

class SavingsAccount(Account):

    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)

    def __str__(self):
        return "{}'s Saving's Account balance is:{}".format(self.name,self.balance)

c=SavingsAccount('Aditya',10000)
print(c)
c.deposit(250000)
print(c)
c.withdraw(100000)
print(c)
print()
s=CurrentAccount('Aniketh',350000)
print(s)
s.deposit(250000)
print(s)
s.withdraw(200200)
print(s)

