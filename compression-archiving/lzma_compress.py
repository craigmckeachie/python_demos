import lzma
import shutil

with open("./colors.txt", "rb") as source_file:
    with lzma.open("colors.txt.xz", "wb") as target_file:
        shutil.copyfileobj(source_file, target_file)
