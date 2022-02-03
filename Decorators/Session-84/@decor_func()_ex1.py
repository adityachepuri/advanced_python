def decor(func): # We can give any name to the in the place of decor & func
    def Inner():
        print('#'*20)
        print('Sachin is the best batsmen')
        print('Kapil Dev is the best bowler')
        func()
        print('#'*20)
    return Inner

@decor
def f():
    print('Accepted')

@decor
def f():
    print('I dont accept')


f()
f()
