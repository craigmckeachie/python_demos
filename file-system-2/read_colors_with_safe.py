from pathlib import Path

from safe_fs import safe_open

colors_path = Path.cwd().joinpath("colors.txt")
colors_file = None

with safe_open(colors_path, "r") as (colors_file, exc):
    if exc:
        print(exc)
    else:
        for color in colors_file:
            print(color.rstrip())
