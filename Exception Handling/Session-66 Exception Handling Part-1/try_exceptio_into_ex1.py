try:
    print(10/0)
except ZeroDivisionError as msg:
    print('Exception raised and its description is:', msg)
