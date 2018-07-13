"""
@name: 
@author: QuocVietIT
@version: 1.0
@since: 
"""

import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# Language
LANGUAGE = "english"

# Setup logging
LOGGING_FILE_PATH = os.path.join(DIR_PATH, 'logs')
LOGGING_CONTENT_FORMAT = "%(asctime)s [%(threadName)s] [%(levelname)s] - %(message)s"
LOGGING_DATE_FORMAT = "%d/%m/%Y %I:%M:%S %p"
LOGGING_FILE_NAME_FORMAT = "{}\log-{}.txt"