from pathlib import Path
colors_path = Path.cwd().joinpath("colors2.txt")
colors_file = None

try:
    with open(colors_path, "r") as colors_file:
        for color in colors_file:
            print(color.rstrip())

except FileNotFoundError:
    print(f"{colors_path.name} was not found")
except IOError as exc:
    print(exc)
