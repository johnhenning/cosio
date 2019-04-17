import json
import os
from functools import reduce


def is_file(filename):
    _, ext = os.path.splitext(filename)
    return ext != ''


def load_credentials(filename):
    with open(filename) as f:
        return json.load(f)


def get_files_from_directory(directory):
    filenames = [[os.path.join(root, f) for f in files] for root, _, files in os.walk(directory)]
    return reduce(lambda x, y: x + y, filenames, [])


def merge_local_and_remote_paths(local_files, local_directory, remote_directory):
    return [os.path.join(remote_directory, os.path.relpath(local_file, local_directory))
            for local_file in local_files]
