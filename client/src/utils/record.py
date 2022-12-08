from src.utils.file import *
import settings


def load_record():
    record = []
    result = load_json_file(f"{settings.BASE_DIR}/.local/record.json")
    record = result if result else record
    return record
    
def save_record(record):
    dump_json_file(record, f"{settings.BASE_DIR}/.local/record.json")

def find_best_record():
    best_score = 0
    record = load_record()
    for i in record:
        if i["score"] >= best_score:
            best_score = i["score"]
            best_record = i
    return best_record

