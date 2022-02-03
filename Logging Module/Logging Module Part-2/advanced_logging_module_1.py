import logging
logger=logging.getLogger('demologger')
logger.setLevel(logging.INFO) # Setting the logging level as INFO
consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)#As logging level is already set to INFO, it is not required to set console handler to INFO
formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
logger.debug('Debug Message')
logger.info('Info Message')
logger.warning('Warning Message')
logger.error('Error Message')
logger.critical('Critical Message')
