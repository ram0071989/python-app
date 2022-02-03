import logging
import sys


class AppLogging:

    def __init__(self, name: str):
        log_format = '%(asctime)s - %(funcName)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(log_format)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(stream_handler)
        self.logger.propagate = False

    def info(self, message: str):
        self.logger.info(message)

    def debug(self, message: str):
        self.logger.debug(message)

    def error(self, message: str):
        self.logger.error(message)

    def warn(self, message: str):
        self.logger.warning(message)
