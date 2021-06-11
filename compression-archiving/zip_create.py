from pathlib import Path
from zipfile import ZipFile

data_files_path = Path("./data-files")
data_files_path_zip_path = Path("./data-files.zip")

with ZipFile(data_files_path_zip_path, "w") as data_files_zip:
    for data_file in data_files_path.iterdir():
        data_files_zip.write(data_file, arcname=data_file.name)
