import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from typing import Union

from logger.logger_config import LoggerConfig


class Logger:
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __handler1 = RotatingFileHandler(
        LoggerConfig.LOGS_FILE_NAME, maxBytes=LoggerConfig.MAX_BYTES, backupCount=LoggerConfig.BACKUP_COUNT
    )
    __handler2 = logging.StreamHandler(sys.stdout)
    __formatter = logging.Formatter(LoggerConfig.FORMAT)
    __handler1.setFormatter(__formatter)
    __handler2.setFormatter(__formatter)
    __logger.addHandler(__handler1)
    __logger.addHandler(__handler2)

    @staticmethod
    def set_logger(level: Union[int, str]) -> None:
        Logger.__logger.setLevel(level)

    @staticmethod
    def info(msg: str) -> None:
        Logger.__logger.info(msg)

    @staticmethod
    def debug(msg: str) -> None:
        Logger.__logger.debug(msg)

    @staticmethod
    def warning(msg: str) -> None:
        Logger.__logger.warning(msg)

    @staticmethod
    def error(msg: str) -> None:
        Logger.__logger.error(msg)

    @staticmethod
    def fatal(msg: str) -> None:
        Logger.__logger.fatal(msg)

    @staticmethod
    def step(msg: str) -> None:
        Logger.__logger.info(msg)
