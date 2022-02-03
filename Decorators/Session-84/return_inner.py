def outer():
    print('Outer function started')
    def inner():
        print('Inner function execution')
    print('Outer function returing inner function')
    return inner
i=outer()
i()
