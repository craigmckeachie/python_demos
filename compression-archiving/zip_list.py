from pathlib import Path
from zipfile import ZipFile

data_files_zip_file = Path("./data-files.zip")

# with ZipFile(data_files_zip_file) as data_files_zip:
#     data_files_zip.extractall()

with ZipFile(data_files_zip_file) as data_files_zip:
    for member_name in sorted(data_files_zip.namelist()):
        print(member_name)
