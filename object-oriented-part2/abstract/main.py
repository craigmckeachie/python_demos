# from text_logger import TextLogger

# logger = TextLogger("log.txt")

from csv_logger import CsvLogger


logger = CsvLogger('log.csv')
logger.log("some message")
