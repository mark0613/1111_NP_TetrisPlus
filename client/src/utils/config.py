from src.utils.file import *
import settings

def load_config():
    config = {
        "isZen" : False,
        "speed" : 1
    }
    result = load_json_file(f"{settings.BASE_DIR}/.local/config.json")
    config = result if result else config
    return config

def save_config(config):
    dump_json_file(config, f"{settings.BASE_DIR}/.local/config.json")

