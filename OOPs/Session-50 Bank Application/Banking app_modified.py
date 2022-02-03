import sys
class Customer:
    '''Customer class with bank operations'''

    bankname='State Bank of India'

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

name=input('Enter your name:')
print('Welcome to', Customer.bankname)
c=Customer(name)
while True:
        print("d-Deposit \nw-withdrawl \ne-Exit")
        option=input('Choose your option:').upper()
        if option=='d':
            amount=float(input("Enter amount to deposit:"))
            c.deposit(amount)
            print("Thank you for Banking with us")
        elif option=='w':
            while True:
                amount=float(input('Enter amount to withdraw:'))
                if not(amount%100==0 and amount < 500):
                   print("Minimum Balance of 500 is necessary")
                else:
                    break 
            sys.exit()
            c.withdrawl(amount)
        elif option=='e':
            print('Thanks for Banking')
            sys.exit()
        else:
            print('Invalid option ....please valid option')
