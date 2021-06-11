from pathlib import Path
colors_path = Path.cwd().joinpath("colors.txt")
colors_file = None

try:

    colors_file = open(colors_path, "r")

    for color in colors_file:
        print(color.rstrip())
except FileNotFoundError:

    print(f"{colors_path.name} was not found")

finally:
    if colors_file:
        colors_file.close()
