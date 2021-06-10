from pathlib import Path

sample_files_path = Path.cwd().joinpath("sample-files")

for member in sample_files_path.iterdir():
    print(member.name, "dir: ", member.is_dir(), "file:", member.is_file())
