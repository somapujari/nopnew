import logging


class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        file = logging.FileHandler(r'C:\Users\Dell\PycharmProjects\mercurynew\logs\auto_nop_login.log')
        formater = logging.Formatter(' %(message)s: %(asctime)s  : %(levelname)s : %(funcName)s : %(levelno)s')
        file.setFormatter(formater)
        logger.addHandler(file)
        return logger


