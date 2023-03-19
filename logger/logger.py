from datetime import datetime
from glob import glob
import logging
import logging.handlers
import os
import sys

from utility.singleton import SingletonInstane


class LogLevel:
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0


class Logger(SingletonInstane):
    def __init__(self, log_level=logging.DEBUG, max_log_count=10):
        self.logger = logging.getLogger('logger')

        # make log folder
        log_folder = '.log'
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # remove old logs
        logs = list(glob("{}/*.log".format(log_folder)))
        logs.sort()
        log_count = len(logs)
        if max_log_count <= log_count:
            remove_count = log_count - max_log_count + 1
            for log_file in logs[:remove_count]:
                os.remove(log_file)

        now = datetime.now()
        log_file_name = '%04d%02d%02d_%02d%02d%02d_%06d.log' % (now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
        log_file_path = os.path.join(log_folder, log_file_name)

        fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s> %(message)s')
        file_handler = logging.FileHandler(log_file_path, mode='w')
        file_handler.setFormatter(fomatter)
        file_max_byte = 1024 * 1024 * 10  # 100MB
        file_handler = logging.handlers.RotatingFileHandler(log_file_path, maxBytes=file_max_byte, backupCount=10)
        self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(fomatter)
        self.logger.addHandler(stream_handler)

        self.logger.setLevel(log_level)
        sys.stderr = self

    def write(self, data):
        self.logger.info(data.rstrip())

    def info(self, data):
        self.logger.info(data)

    def warning(self, data):
        self.logger.warning(data)

    def error(self, data):
        self.logger.error(data)

    def critical(self, data):
        self.logger.critical(data)

    def test(self):
        self.info("TEST START")
        self.warning("스트림으로 로그가 남아요~")
        self.error("파일로도 남으니 안심이죠~!")
        self.critical("치명적인 버그는 꼭 파일로 남기기도 하고 메일로 발송하세요!")
        self.info("TEST END!")
