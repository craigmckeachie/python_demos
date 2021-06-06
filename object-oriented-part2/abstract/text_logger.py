from datetime import datetime
from logger import Logger


class TextLogger(Logger):

    def __init__(self, file_name):
        self._file_name = file_name

    def log(self, entry):

        with open(self._file_name, "a") as log_file:
            log_file.write(f"{datetime.now()} {entry}\n")
