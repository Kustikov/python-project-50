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
            result.append({"name": key, "value": dict_2[key], "type": "added"})
        elif key not in keys_2:
            result.append({"name": key, "value": dict_1[key], "type": "deleted"})
        elif dict_1[key] == dict_2[key]:
            result.append({"name": key, "value": dict_1[key], "type": "unchanged"})
        elif dict_1[key] != dict_2[key]:
            result.append(
                {
                    "name": key,
                    "value1": dict_1[key],
                    "value2": dict_2[key],
                    "type": "changed",
                }
            )
    print(result)
    return result


def formatter(diff):
    print(diff)
    result = ""
    for key in diff:
        for i in diff[key]:
            result = f"{result}{key} {i}\n"
    result = result.split("\n")
    start_index = 2
    end_index = 3
    result.sort(key=lambda by_name: by_name[start_index:end_index])
    answer = "\n".join(result)
    print(f"{{{answer}\n}}")
    return answer
