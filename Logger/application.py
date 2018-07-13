import logging
from Logger.utils.logger_initializer import initialize_logger

if __name__ == '__main__':
    initialize_logger()

    # Test
    #Write to console and file
    logging.info("This is a logger info")
    logging.error("Error")
    logging.warning("Warning")

    #Write to file
    logging.debug("Debug")

