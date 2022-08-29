import os

from features.helper.logger import Logger
import logging
from utility.file_handler import create_dir
log = Logger('mysys.log').get_logger()


def before_all(context):
    # Creating report directory
    log.info("Creating report directory")
    create_dir(os.path.abspath('../reports'))

    """Initialise Logger"""
    log.addHandler(logging.StreamHandler())
    log.setLevel(logging.DEBUG)
    log.info("Test started")


