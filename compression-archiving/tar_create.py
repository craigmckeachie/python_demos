import tarfile

# with tarfile.open("./data-files.tar", "w") as data_files_tar:
#     data_files_tar.add("./data-files")


with tarfile.open("./data-files.tar.gz", "w:gz") as data_files_tar:
    data_files_tar.add("./data-files")
