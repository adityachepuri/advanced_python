def Sunnydecor(f1):
    def inner(name):
        if name=='Sunny':
            print('#'*20)
            print('Hello Sunny Good evening...')
            print('You are so great...all VIP facilities are available')
            print('#'*20)
        else:
            f1(name) 
    return inner

@Sunnydecor
def wish(name):
    print('Hello',name,'Good Evening !!!')

wish('durga')
wish('Sunny')
