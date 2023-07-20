import json
import yaml


def get_dict(path):
    if path.endswith(".json"):
        with open(f"{path}", "r", encoding="utf-8") as file:
            return json.load(file)
    elif path.endswith(".yml") or path.endswith(".yaml"):
        with open(f"{path}", "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    else:
        raise ValueError('Unsupported format. '
                         'Formats are supported: .json .yaml .yml')


def change_type(dict):
    new_dict = {}
    for key, value in dict.items():
        if isinstance(value, type(dict)):
            new_dict[key] = change_type(value)
        elif isinstance(value, bool):
            new_dict[key] = str(value).lower()
        elif value is None:
            new_dict[key] = 'null'
        else:
            new_dict[key] = value
    return new_dict


def generate_diff(data1, data2):
    diff = {}
    keys = sorted(set(data1.keys()).union(data2.keys()))
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = generate_diff(value1, value2)
        elif value1 is None and value2 is not None:
            diff.setdefault(key, ['added']).append(value2)
        elif value1 is not None and value2 is None:
            diff.setdefault(key, ['deleted']).append(value1)
        elif value1 == value2:
            diff.setdefault(key, ['unchanged']).append(value1)
        else:
            diff.setdefault(key, ['changed']).append(value1)
            diff[key].append(value2)
    result_file = open("diff.txt", "w")
    result_file.write(str(diff))
    result_file.close()
    return diff
