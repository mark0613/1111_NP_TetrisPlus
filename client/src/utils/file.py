import os
import json


def loadJsonFile(path):
    result = None
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            result = json.load(file)
    return result

def dumpJsonFile(data, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)
