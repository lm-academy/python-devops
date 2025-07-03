import logging
import logging.config
import json
from typing import Any, Dict

"""
# Uncomment to test INI configuration

# Declarative logging configuration - INI-file
print("Declarative configuration using INI files")
print("---------\n")

config_path = "declarative-config.ini"

logging.config.fileConfig(
    fname=config_path,
)

app_logger = logging.getLogger("app")
app_logger.debug("INI-style fileConfig is working!")
"""

"""
# Uncomment to test Dictionary configuration

# Declarative logging configuration - Dictionary config
print("Declarative configuration using dictionary config")
print("---------\n")

dict_config: Dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(levelname)-8s - %(message)s"}
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "config.dict": {
            "level": "DEBUG",
            "handlers": ["console"],
        }
    },
}

logging.config.dictConfig(dict_config)
config_logger = logging.getLogger("config.dict")
config_logger.debug("dictConfig setup successfully")
config_logger.info("Info goes to console")
"""

"""
# Uncomment to test JSON configuration

# Declarative logging configuration - JSON config
print("Declarative configuration using JSON config")
print("---------\n")

config_path = "declarative-config.json"

with open(config_path, "r") as config_file:
    json_config = json.load(config_file)

logging.config.dictConfig(json_config)
config_logger = logging.getLogger("config.json")
config_logger.debug("JSON config setup successfully")
config_logger.info("Info goes to console")
"""

# Dynamically building config
print("Dynamically building config")
print("---------\n")

base_config: Dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": True,
    "handlers": {},
    "formatters": {},
    "loggers": {},
}

base_config["formatters"]["simple"] = {
    "format": "%(levelname)-8s - %(message)s"
}

base_config["handlers"]["console"] = {
    "class": "logging.StreamHandler",
    "level": "DEBUG",
    "formatter": "simple",
    "stream": "ext://sys.stdout",
}

base_config["loggers"]["config.dynamic"] = {
    "level": "WARNING",
    "handlers": ["console"],
}


def is_debug():
    return True


if is_debug():
    for logger, _config in base_config["loggers"].items():
        base_config["loggers"][logger]["level"] = "DEBUG"


logging.config.dictConfig(base_config)
config_logger = logging.getLogger("config.dynamic")
config_logger.debug("Dynamic config setup successfully")
config_logger.info("Info goes to console")
