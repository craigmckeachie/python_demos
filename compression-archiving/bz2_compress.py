import bz2
import shutil

with open("./colors.txt", "rb") as source_file:
    with bz2.open("colors.txt.bz2", "wb") as target_file:
        shutil.copyfileobj(source_file, target_file)
