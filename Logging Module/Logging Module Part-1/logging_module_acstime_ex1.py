import logging
logging.basicConfig(filename='log_20200625-write mode.txt',format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p',filemode='w')
logging.debug('Debug Message')
logging.info('Info Message')
logging.warning('Warning Message')
logging.error('Error Message')
logging.critical('Critical Message')
print('logging Demo')
