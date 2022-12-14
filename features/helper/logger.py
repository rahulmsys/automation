import logging


class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        self.file_handler = logging.FileHandler(self.log_file)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)

    def critical(self, message):
        self.logger.critical(message)

    def debug(self, message):
        self.logger.debug(message)

    def exception(self, message):
        self.logger.exception(message)

    def get_logger(self):
        return self.logger
