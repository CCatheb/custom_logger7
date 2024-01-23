import logging

class CustomFormatter(logging.Formatter):

    FORMATS = {
        logging.DEBUG: "[%(levelname)s][%(name)s] - [%(filename)s, %(lineno)d] - [%(threadName)s]: %(message)s",
        logging.INFO: "[%(levelname)s][%(name)s]: %(message)s",
        logging.WARNING: "[%(levelname)s][%(name)s]: %(message)s",
        logging.ERROR: "[%(levelname)s][%(name)s]: %(message)s",
        logging.CRITICAL: "[%(levelname)s][%(name)s]: %(message)s"
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class CustomLogger:
    def __init__(self, name, level=logging.DEBUG, log_to_console=True, log_to_file=True, log_file_path=None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        if log_file_path is None:
            log_file_path = f'/var/log/{name}.log'

        # Création du gestionnaire de la console
        if log_to_console:
            ch = logging.StreamHandler()
            ch.setLevel(level)
            formatter = CustomFormatter()
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

        # Création du gestionnaire de fichier
        if log_to_file:
            fh = logging.FileHandler(log_file_path)
            fh.setLevel(level)
            formatter = CustomFormatter()
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
