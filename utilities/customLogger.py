import logging


def create_logger(filename, filemode, level=logging.DEBUG):
    logger = logging.getLogger('custom_logger')
    logger.setLevel(level=level)
    formatter = logging.Formatter(datefmt='%m-%d-%Y %I:%M:%S %p',
                                  fmt="%(asctime)s - %(name)s - %(filename)s | %(levelname)s : %(message)s")
    file_handler = logging.FileHandler(filename=filename,
                                        mode=filemode)
    file_handler.setFormatter(fmt=formatter)
    logger.addHandler(file_handler)
    return logger