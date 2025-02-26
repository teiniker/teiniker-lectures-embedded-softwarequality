import logging

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s : %(message)s')
logging.basicConfig(level=logging.WARNING, filename='example.log',
    format='%(asctime)s %(levelname)s %(name)s : %(message)s')
log = logging.getLogger(__name__)

log.debug('This is a debug message')
log.info('This is an info message')
log.warning('This is a warning message')    # default level
log.error('This is an error message')
log.critical('This is a critical message')
