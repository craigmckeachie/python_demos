from pathlib import Path

current_working_directory = Path.cwd()

print(current_working_directory)
print(type(current_working_directory))

home_directory = Path.home()
print(home_directory)
print(type(home_directory))
