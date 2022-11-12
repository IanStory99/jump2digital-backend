import logging


def register_logger():
    logger = logging.getLogger("root")
    logger.setLevel(logging.DEBUG)

    f_handler = logging.FileHandler('./logs/applogs.log')
    f_handler.setLevel(logging.INFO)

    f_format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    f_handler.setFormatter(f_format)

    logger.addHandler(f_handler)
    return logger
