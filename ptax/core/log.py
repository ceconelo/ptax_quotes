import logging.config
'''
    Available Handlers Name
    root
    console
'''


def log(handler_name):
    logging.config.fileConfig(fname='settings.ini')
    logger = logging.getLogger(handler_name)
    return logger