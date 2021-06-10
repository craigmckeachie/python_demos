from pathlib import Path

current_working_directory = Path.cwd()
sample_files_path = current_working_directory.joinpath('sample-files')
print(sample_files_path)


