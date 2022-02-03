import logging
logger=logging.getLogger('Demo Logger')
logger.setLevel(logging.INFO)

consoleHandler=logging.StreamHandler()
fileHandler = logging.FileHandler('abc369.txt')
fileHandler.setLevel(logging.ERROR)

formatter=logging.Formatter('%(asctime)s-%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p'
'%d/%m/%Y %I:%M:%S %p')

formatter1=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S')

consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter1)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

logger.debug('Debug Message')
logger.info('Info Message')
logger.warning('Warning Message')
logging.error('Error Message')
logger.critical('Critical Message')
