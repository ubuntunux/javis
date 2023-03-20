import configparser
from glob import glob
import os

from kivy.config import Config
from kivy.utils import platform


def clear_logs(log_folder):
    log_maxfiles = 10
    logs = list(glob("{}/*.log".format(log_folder)))
    logs.sort()
    log_count = len(logs)
    if log_maxfiles <= log_count:
        remove_count = log_count - log_maxfiles + 1
        for log_file in logs[:remove_count]:
            os.remove(log_file)


def initialize_config(log_folder):
    Config.read('config.ini')
    Config.set('kivy', 'log_level', 'info')
    Config.set('kivy', 'log_enable', 1)
    Config.set('kivy', 'log_name', '%Y%m%d_%H%M%S_%_.log')
    Config.set('kivy', 'log_dir', log_folder)
    Config.write()


def run_app():
    log_folder = os.path.abspath('.log')

    clear_logs(log_folder)

    # Note: Config must be set before import kivy.logger
    initialize_config(log_folder)

    # android permission
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

    # run app
    from javis.javis import JavisApp
    JavisApp().run()
    Config.write()


if __name__ == '__main__':
    run_app()
