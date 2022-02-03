import sys
class Customer:
    '''Customer class with bank operations'''

    bankname='SHREERAM ADITYA'

    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('The Balance after deposit is:',self.balance)

    def withdrawl(self,amount):
        if amount > self.balance:
            print("insufficient funds ...cannot perform this operation")
            sys.exit()
        self.balance=self.balance-amount
        print("The balance in after withdrawl:",self.balance)

print('Welcome to',Customer.bankname)
name=input('Enter your name:')
c=Customer(name)
while True:
        print("d-Deposit \nw-withdrawl \ne-Exit")
        option=input('Choose your option:').lower()
        if option=='d':
            amount=float(input("Enter amount to deposit:"))
            c.deposit(amount)
        elif option=='w':
            amount=float(input('Enter amount to withdraw:'))
            c.withdrawl(amount)
        elif option=='e':
            print('Thanks for Banking')
            sys.exit()
        else:
            print('Invalid option ....please valid option')
        
