def smart_division(func):
    def inner(a,b):
        print('We are dividing {} with {}'.format(a,b))
        if b==0:
            print('Hello stupid how can we divide with zero???')
            return
        else:
            return func(a,b)
    return inner

@smart_division
def division(a,b):
    return a*b

print(division(20,2))
print(division(20,0))
