from os import getcwd, listdir, mkdir, rmdir
from os.path import join, isfile


# for member in listdir(join(getcwd(), "sample-files")):
#     print(member)

# path = join(getcwd(), "sample-files")

# files_in_sample_files = [member for member in listdir(
#     path) if isfile(join(path, member))]

# print(files_in_sample_files)
# print(sorted(files_in_sample_files))

# mkdir(join(getcwd(), 'temp'))
rmdir(join(getcwd(), 'temp'))
