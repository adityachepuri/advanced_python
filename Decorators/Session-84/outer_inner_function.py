def outer():
    print('Outer function started')
    def inner():
        print('Inner Function execution')
    print('Outer function calling inner function')
    return inner()
outer()
