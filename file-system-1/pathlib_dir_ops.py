from pathlib import Path

path = Path.cwd().joinpath('sample-files')

# for member in path.iterdir():
#     print(member.name)

files_in_sample_files = [
    member.name for member in path.iterdir() if member.is_file()]

print(sorted(files_in_sample_files))

temp_path = Path.cwd().joinpath('temp')
# temp_path.mkdir()
temp_path.rmdir()
print(temp_path)
