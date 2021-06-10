import os
print(os.getcwd())

os.chdir('sample-files')
# os.chdir(r'.\sample-files') errors
print(os.getcwd())
