import bz2

with bz2.open("./colors.txt.bz2", "rb") as compressed_file:
    file_content = compressed_file.read()

    print(file_content.decode("UTF-8"))
