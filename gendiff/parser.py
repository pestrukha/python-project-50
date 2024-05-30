import os
import json
import yaml
from yaml.loader import SafeLoader
import argparse


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


def parse_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')

    # Positional arguments
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    # Optional arguments
    parser.add_argument('-f', '--format',
                        help='set format of output (default: "stylish")')

    args = parser.parse_args()
    return args.first_file, args.second_file
