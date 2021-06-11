from pathlib import Path
from zipfile import ZipFile

data_files = Path("./data-files").glob("**/*")
data_files_zip = Path("./data-files-dir.zip")

print(list(data_files))



with ZipFile(data_files_zip, "w") as zip_file:
    for data_file in data_files:
        zip_file.write(data_file)
