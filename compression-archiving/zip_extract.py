from pathlib import Path
from zipfile import ZipFile

data_files_zip_file = Path("./data-files.zip")

# with ZipFile(data_files_zip_file) as data_files_zip:
#     data_files_zip.extractall()

with ZipFile(data_files_zip_file) as data_files_zip:
    data_files_zip.extractall("data-files2")
