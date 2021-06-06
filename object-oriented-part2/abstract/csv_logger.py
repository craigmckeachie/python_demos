import csv
from datetime import datetime
from logger import Logger


class CsvLogger(Logger):

    def __init__(self, file_name):
        self._file_name = file_name

    def log(self, entry):

        with open(self._file_name, "a") as log_file:
            csv_writer = csv.writer(log_file)
            csv_writer.writerow([datetime.now(), entry])
