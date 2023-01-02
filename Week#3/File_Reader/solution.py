# Реалізація простого класу для читання з файлу
import os

class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        if not os.path.exists(self.path):
            return ""
        with open(self.path, 'r') as inF:
            return inF.read()

