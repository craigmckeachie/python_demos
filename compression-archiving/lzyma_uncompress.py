import lzma

with lzma.open("./colors.txt.xz", "rb") as compressed_file:
    file_content = compressed_file.read()

    print(file_content.decode("UTF-8"))
