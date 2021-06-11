import tarfile


# with tarfile.open("./data-files.tar") as data_files_tar:
#     data_files_tar.extractall()

with tarfile.open("./data-files.tar.gz") as data_files_tar:
    data_files_tar.extractall()
