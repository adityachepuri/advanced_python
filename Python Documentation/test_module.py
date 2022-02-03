'''
This is test module to explain the importance of documentation,
which will play very important role and improves readibility.
Sometimes documentation is bigger than original code
'''


__author__='Aditya'
__copyright__='Copy Right 2020, Aditya'


def add(a,b):
    '''This function meant for arithmatic addition operation will take 2 arguments
    and return the sum'''
    return a+b

def multiply(a,b):
    '''This function meant for arithmatic multiplication. Operation will take
    2 arguments and return the product'''
    return a*b

def main():
    '''This is the main function from here we can call the remaining methods'''
    print(add(10,20))
    print(multiply(10,20))

x=888
y=999

if __name__=='main':
    main()
    
