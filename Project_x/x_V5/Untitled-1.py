# import structlog


# log = structlog.get_logger()
# log.info("hello, %s!", "world", key="value!", more_than_strings=[1, 2, 3])

#console warning
# logging.warning('Watch out!')  # will print a message to the console WARNING:root:Watch out!
# logging.info('I told you so')


#logging to a file
# import logging
# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logger.debug('This message should go to the log file')
# logger.info('So should this')
# logger.warning('And this, too')
# logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

#date/time logging
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')