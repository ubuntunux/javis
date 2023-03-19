import os

from utility.singleton import SingletonInstane


class Config(SingletonInstane):
    def __init__(self):
        self.file_name = ''
        self.data = {
            'listener_pos': (0, 0)
        }

    def initialize(self, file_name):
        self.file_name = file_name
        self.load()

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

    def save(self):
        with open(self.file_name, 'w') as f:
            f.write(repr(self.data))

    def load(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as f:
                self.data = eval(f.read())
