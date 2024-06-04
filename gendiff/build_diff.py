def build_diff(d1, d2):
    diff = []
    all_keys = set(d1.keys()).union(d2.keys())

    for key in sorted(all_keys):
        if key not in d2:
            diff.append({'key': key, 'status': 'removed', 'old_value': d1[key]})
        elif key not in d1:
            diff.append({'key': key, 'status': 'added', 'new_value': d2[key]})
        elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
            nested_diff = build_diff(d1[key], d2[key])
            diff.append({'key': key, 'status': 'nested', 'nested': nested_diff})
        elif d1[key] != d2[key]:
            diff.append({'key': key, 'status': 'updated', 'old_value': d1[key], 'new_value': d2[key]})
        else:
            diff.append({'key': key, 'status': 'unchanged', 'old_value': d1[key]})

    return diff