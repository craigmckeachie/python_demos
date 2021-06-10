from os import getcwd
from os.path import join

path = join(getcwd(), 'sample-files', 'test')  # does work on POSIX and Windows
# path = join(getcwd(), r'sample-files\test') # doesn't work on windows
print(path)
