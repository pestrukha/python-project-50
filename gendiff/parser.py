import os
import json
import yaml
from yaml.loader import SafeLoader


def parse_json(file1, file2):
    f1, f1_extension = os.path.splitext(file1)
    f2, f2_extension = os.path.splitext(file2)
    data1, data2 = None, None
    if f1_extension == '.json':
        with open(file1) as f:
            data1 = json.load(f)
    if f2_extension == '.json':
        with open(file2) as f:
            data2 = json.load(f)
    if data1 is None or data2 is None:
        return False
    return data1, data2


def parse_yaml(file1, file2):
    f1, f1_extension = os.path.splitext(file1)
    f2, f2_extension = os.path.splitext(file2)
    data1, data2 = None, None
    if f1_extension in ['.yml', '.yaml']:
        with open(file1) as f:
            data1 = yaml.load(f, Loader=SafeLoader)
    if f2_extension in ['.yml', '.yaml']:
        with open(file2) as f:
            data2 = yaml.load(f, Loader=SafeLoader)
    if data1 is None or data2 is None:
        return False
    return data1, data2
