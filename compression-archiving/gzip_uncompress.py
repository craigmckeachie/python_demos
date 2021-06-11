import gzip

with gzip.open("./colors.txt.gz", "rb") as compressed_file:
    file_content = compressed_file.read()

    print(file_content.decode("UTF-8"))
