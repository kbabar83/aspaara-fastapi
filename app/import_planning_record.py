import json
from pathlib import Path
import os
from . import models
from config.database import get_db
import datetime


BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


def upload_file(file_object):
    """
    Function to read file records.
    """
    file_name = "planning_files" + "/" + file_object.filename
    files = os.path.join(MEDIA_ROOT, file_name)
    with open(files, "wb+") as file_data:
        file_data.write(file_object.file.read())
        file_data.close()
    return files


def process_record(planning_file):
    """
    Function to upload file records in database.
    """
    json_file = upload_file(planning_file)
    record_file = open(json_file, "r")
    data = json.loads(record_file.read())
    sessions = get_db()

    record_list = []
    for record in data:
        record["startDate"] = datetime.datetime.strptime(
            record["startDate"], "%m/%d/%Y %I:%M %p"
        )
        record["endDate"] = datetime.datetime.strptime(
            record["endDate"], "%m/%d/%Y %I:%M %p"
        )
        record_list.append(models.Record(**record))

    sessions.bulk_save_objects(record_list)
    sessions.commit()
