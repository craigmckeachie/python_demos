from os import listdir, getcwd
from os.path import join, isdir, isfile

path = join(getcwd(), "sample-files")

for member in listdir(path):
    print(member, "is dir:", isdir(join(path, member)),
          "is file:", isfile(join(path, member)),
          )
