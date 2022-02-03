try:
    print('Outer try block')

    try:
        print('Inner try block')
        print(10/0)

    except ArithmatiError:
        print('Inner except block')

    finally:
        print('Inner Finally block')

except:
    print('Outer except block')

finally:
    print('Outer finally block')
