import json
import os.path


def is_file(filename):
    _, ext = os.path.splitext(filename)
    return ext != ''


def load_credentials(filename):
    with open(filename) as f:
        return json.load(f)
