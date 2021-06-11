from pathlib import Path
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read(Path.cwd().joinpath("web.ini"))

cfg.add_section("WebServer")
cfg.set("WebServer", "port", "8090")

cfg.add_section("DatabaseServer")
cfg.set("DatabaseServer", "user", "dbuser")


with open("web.ini", "w") as cfg_file:
    cfg.write(cfg_file)
