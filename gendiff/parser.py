import json
import yaml
import os


def parse_data(file, extension):
    if extension == '.json':
        return json.loads(file)
    elif extension in ['.yml', '.yaml']:
        return yaml.load(file, Loader=yaml.Loader)
    else:
        raise ValueError(f'Unsupported file format: {extension}')


def get_data(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    with open(file_path) as file:
        return parse_data(file.read(), extension)
