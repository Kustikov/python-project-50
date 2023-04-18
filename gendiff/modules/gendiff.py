import json
import yaml


def get_dict(path):
    if path.endswith(".json"):
        with open(f"{path}", "r", encoding="utf-8") as file:
            return json.load(file)
    elif path.endswith(".yml") or path.endswith(".yaml"):
        with open(f"{path}", "r", encoding="utf-8") as file:
            return yaml.safe_load(file)


def generate_diff(dict_1, dict_2):
    result = {}
    keys_1 = dict_1.keys()
    keys_2 = dict_2.keys()
    common_keys = keys_1 & keys_2
    deleted_keys = keys_1 - keys_2
    added_keys = keys_2 - keys_1
    for key in common_keys:
        if isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
            result[key] = {
                "type": "nested",
                "value": generate_diff(dict_1[key], dict_2[key]),
            }
        elif dict_1[key] == dict_2[key]:
            result[key] = {"type": "unchanged", "value": dict_1[key]}
        else:
            result[key] = {
                "type": "changed",
                "old_value": dict_1[key],
                "value": dict_2[key],
            }
    new_dict = {}
    for key in deleted_keys:
        new_dict[key] = {"type": "deleted", "value": dict_1[key]}
        result.update(new_dict)
    for key in added_keys:
        new_dict[key] = {"type": "added", "value": dict_2[key]}
        result.update(new_dict)
    sorted_result = dict(sorted(result.items()))
    stylish(sorted_result)
    return result


def stylish(data):
    result = ""
    for i, v in data.items():
        print(v["value"])
        current_type = v["type"]
        current_name = i
        if current_type == "deleted":
            result += f'- {current_name} {v["value"]}\n'
        elif current_type == "unchanged":
            result += f'  {current_name} {v["value"]}\n'
        elif current_type == "changed":
            result += f'- {current_name} {v["value"]} \
                    \n+ {current_name} {v["old_value"]}\n'
        elif current_type == "added":
            result += f'+ {current_name} {v["value"]}\n'
    print(f"{{\n{result}}}")
