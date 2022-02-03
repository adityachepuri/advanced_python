import logging
logging.basicConfig(filename='log_20200625-log mod info.txt',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%H:%M:%S')
logging.info('A New request came')
try:
    x=int(input('Enter First Number'))
    y=int(input('Enter Second Number'))
    print(x/y)

except ZeroDivisionError as msg:
    print('Cannot divide with Zero')
    logging.exception(msg)

except ValueError as msg:
    print('Please provide int values only')
    logging.exception(msg)

logging.info('Request processing completed')
