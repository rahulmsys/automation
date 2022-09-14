import os
import logging
import datetime as dt


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Only create a new instance if one does not exist
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonType):
    _logger = None

    def __int__(self, log_dir=os.environ.get('BEYONDHR_HOME', None), file_name=''):
        self._logger = logging.getLogger("beyondhr")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        now = dt.datetime.now()
        if log_dir:
            dirname = os.path.join(log_dir, 'logs')
        else:
            current_path = os.getcwd()
            dirname = os.path.join(current_path[:current_path.find('beyondhr')], 'beyondhr', 'logs')

        if not os.path.isdir(dirname):
            os.makedirs(dirname)

        if not file_name:
            file_name = os.path.join(dirname, 'z_{0}.log'.format(now.strftime("%y-%-m-%d")))
        fileHandler = logging.FileHandler(file_name)

        if os.path.isfile(file_name):
            try:
                os.chmod(file_name, 0o777)
            except OSError:
                pass

        # Also create a stream handler, logging is also displayed on console output
        streamHandler = logging.StreamHandler()
        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)
        streamHandler.setLevel(logging.INFO)
        logging.getLogger('chardet.charsetprober').setLevel(logging.INFO)

    def get_logger(self):
        return self._logger


def logged(func):
    """
    This function will be used as a decorator for logging all the function calls.
    Wherever we want to see the transactional details.
    Basic details can be easily captured from logs itself
    """

    log = Logger.__call__().get_logger()

    def run(*args, **kwargs):
        log.info("trans_start | {0}".format(func.__name__))
        out = func(*args, **kwargs)
        log.info("trans_end | {0}".format(func.__name__))
        return out

    return run
