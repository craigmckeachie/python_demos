from pathlib import Path
from safe_fs2 import safe_open

colors = ['red', 'green', 'blue']

new_colors_path = Path.cwd().joinpath('newcolors.txt')
with safe_open(new_colors_path, "a") as (new_colors_file, exc):
    if exc:
        print(exc)
    else:
        for color in colors:
            new_colors_file.write(f"{color}\n")
