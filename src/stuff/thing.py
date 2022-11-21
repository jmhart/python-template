import logging

logger = logging.getLogger(__name__)


def do_something():
    logger.debug(
        'Detailed information, typically of interest only when diagnosing problems.')
    logger.info('Confirmation that things are working as expected.')
    logger.warning(
        'An indication that something unexpected happened. The software is still working as expected.')
    logger.error(
        'Due to a more serious problem, the software has not been able to perform some function.')
    logger.critical(
        'A serious error, indicating that the program itself may be unable to continue running.')


def fail_something():
    raise SystemError()
