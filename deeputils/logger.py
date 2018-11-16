import logging
import os
import sys
from datetime import datetime

from django.utils.termcolors import colorize


class Formatter(logging.Formatter):
    color = {
        logging.DEBUG: 'cyan',
        logging.INFO: 'green',
        logging.WARNING: 'yellow',
        logging.ERROR: 'red',
        logging.CRITICAL: 'magenta',
    }

    def format(self, record):
        original = self._style._fmt
        self._style._fmt = colorize('[%(asctime)s] ', fg=self.color[record.levelno]) + '%(message)s'
        result = logging.Formatter.format(self, record)
        self._style._fmt = original
        return result


def setup_log(level=logging.DEBUG, path=None, tag: str = None):
    # Stream handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(Formatter())
    logging.root.addHandler(handler)
    # File handler
    if path is not None:
        if not os.path.exists(path):
            os.makedirs(path)
        handler = logging.FileHandler("{}/{}{}.log".format(path, tag + '-' if tag is not None else '', datetime.utcnow().timestamp()))
        handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
        logging.root.addHandler(handler)
    # Set logging level
    logging.root.setLevel(level)


if __name__ == "__main__":
    setup_log(path='./log/', tag='deeputils')
    logging.getLogger().debug('The logging module has been a part of Python’s Standard Library since version %.1f.', 2.3)
