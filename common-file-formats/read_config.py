from pathlib import Path
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read(Path.cwd().joinpath("web.cfg"))

# print(cfg["WebServer"]["port"])
# print(cfg["WebServer"]["path"])

for section_name in cfg:
    print(section_name)
    for setting_name in cfg[section_name]:
        print(setting_name, cfg[section_name][setting_name])
