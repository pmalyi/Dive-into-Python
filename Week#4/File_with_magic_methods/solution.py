# Файли з магічними методами
import os
import tempfile
import datetime


class File:
    def __init__(self, filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as infile:
                infile.write('')
        self.filename = filename

    def __str__(self):
        return self.filename

    def read(self):
        with open(self.filename, 'r', encoding='utf-8') as infile:
            result = infile.read()
        return result

    def write(self, sometext):
        with open(self.filename, 'w', encoding='utf-8') as infile:
            infile.write(sometext)

    def __add__(self, other):
        path_to_new_file = os.path.join(tempfile.gettempdir(), str(datetime.datetime.now()))
        with open(path_to_new_file, 'w', encoding='utf-8') as resfile:
            resfile.write(self.read() + other.read())
        return File(path_to_new_file)

    def __getitem__(self, item):
        with open(self.filename, 'r', encoding='utf-8') as iterfile:
            lines = iterfile.readlines()
        return lines[item]
