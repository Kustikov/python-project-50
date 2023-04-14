import json
import yaml


def get_dict(path):
    if path.endswith(".json"):
        with open(f"{path}", "r", encoding="utf-8") as file:
            return json.load(file)
    elif path.endswith(".yml") or path.endswith(".yaml"):
        with open(f"{path}", "r", encoding="utf-8") as file:
            return yaml.safe_load(file)


def generate_diff(path1, dict_2):
    result = []
    dict_1 = get_dict(path1)
    dict_2 = get_dict(dict_2)
    result = []
    keys_1 = dict_1.keys()
    keys_2 = dict_2.keys()
    keys = sorted(dict_1.keys() | dict_2.keys())
    for key in keys:
        if key not in keys_1:
            result.append({"name": key, "value": dict_2[key],
                           "type": "added"})
        elif key not in keys_2:
            result.append({"name": key, "value": dict_1[key],
                           "type": "deleted"})
        elif dict_1[key] == dict_2[key]:
            result.append({"name": key, "value": dict_1[key],
                           "type": "unchanged"})
        elif dict_1[key] != dict_2[key]:
            result.append(
                {
                    "name": key,
                    "value1": dict_1[key],
                    "value2": dict_2[key],
                    "type": "changed",
                }
            )
    stylish(result)
    return result


def stylish(data):
    result = ""
    for i in data:
        current_type = i["type"]
        current_name = i["name"]
        if current_type == "deleted":
            result += f'- {current_name} {i["value"]}\n'
        elif current_type == "unchanged":
            result += f'  {current_name} {i["value"]}\n'
        elif current_type == "changed":
            result += f'- {current_name} {i["value1"]} \
                    \n+ {current_name} {i["value2"]}\n'
        elif current_type == "added":
            result += f'+ {current_name} {i["value"]}\n'
    print(f"{{\n{result}}}")
    return result
