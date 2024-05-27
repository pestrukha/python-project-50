import json


def generate_diff(data1, data2):
    with open(data1) as f1, open(data2) as f2:
        file1 = {
            k: str(v).lower() if isinstance(v, bool) else v
            for k, v in json.load(f1).items()
        }
        file2 = {
            k: str(v).lower() if isinstance(v, bool) else v
            for k, v in json.load(f2).items()
        }

    equal = file1 | file2
    lines = ['{']
    for key in sorted(equal.keys()):
        if file1.get(key) == file2.get(key):
            lines.append(f'    {key}: {file1[key]}')
        elif key in file1 and key in file2:
            lines.append(f'  - {key}: {file1[key]}')
            lines.append(f'  + {key}: {file2[key]}')

        elif key in file1 and key not in file2:
            lines.append(f'  - {key}: {file1[key]}')
        elif key in file2 and key not in file1:
            lines.append(f'  + {key}: {file2[key]}')

    lines.append('}')
    return '\n'.join(lines)
