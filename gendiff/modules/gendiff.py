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


def generate_diff(data1, data2):
    diff = {}
    keys = sorted(set(data1.keys()).union(data2.keys()))
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = generate_diff(value1, value2)
            # if nested_diff:
            #     diff[key] = nested_diff
        elif value1 is None and value2 is not None:
            diff[key] = {
                "type": "added",
                "value": value2
            }
        elif value1 is not None and value2 is None:
            diff[key] = {
                "type": "deleted",
                "value": value1
            }
        elif value1 == value2:
            diff[key] = {
                "type": "unchanged",
                "value": value1
            }
        else:
            diff[key] = {
                "type": "changed",
                "old_value": value1,
                "new_value": value2
            }
    result_file = open("diff.txt", "w")
    result_file.write(str(diff))
    result_file.close()
    return diff
