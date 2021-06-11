import gzip
import shutil

with open("./colors.txt", "rb") as source_file:
    with gzip.open("colors.txt.gz", "wb") as target_file:
        shutil.copyfileobj(source_file, target_file)
