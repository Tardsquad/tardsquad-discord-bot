import os

TAG_MATCH_ALL = "*"
CUST_ATTRIB_DEPENDSON_NAME = "Depends On"

CONF_FILE_PATH_XDG = os.getenv("XDG_CONFIG_HOME", os.environ["HOME"] + "/.config") + "/tardsquad-discord-bot/tardsquad-discord-bot.conf"
CONF_FILE_PATH = "~/.tardsquad-discord-bot.conf"
CONF_FILE_NAME_FMT = "tardsquad-discord-bot.conf.template"

CFD_DATA_FILE_FMT = "cfd_{:s}.dat"
