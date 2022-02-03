def decor(func):
    def enhanced_function(a,b):
        print('Adding two numbers function')
        print('*'*50)
        print('First argument:',a)
        print('Second Argument:',b)
        print('THe sum of {} and {} is:{}'.format(a,b,a+b))
        print('*'*50)
    return enhanced_function

# with decorator function
#@decor
#def add(a,b):
    print(a+b)
#add(10,20)
#add(100,200)

#without decorator function
def add(a,b):
    print(a+b)

enhanced_add=decor(add)
add(10,20)
enhanced_add(100,200)
