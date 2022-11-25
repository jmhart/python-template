import logging
import coloredlogs

from . import config
from .stuff import thing


def main():
    config.setup_logging()
    logger = logging.getLogger(__name__)
    coloredlogs.install(level='DEBUG', logger=logger)
    try:
        logger.info('Starting application...')
        start()
    except SystemError as sys_err:
        logger.error(sys_err)
    except Exception as err:
        logger.error(err)
    finally:
        logger.info('Exiting application...')


def start():
    thing.do_something()
