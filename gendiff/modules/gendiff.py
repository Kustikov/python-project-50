import json
import yaml


def get_dict(path):
    if path.endswith('.json'):
        with open(f"{path}", "r", encoding="utf-8") as file:
            return json.load(file)
    elif path.endswith('.yml') or path.endswith('.yaml'):
        with open(f"{path}", "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
        
        

def generate_diff(path1, path2):
    dict_1 = get_dict(path1)
    dict_2 = get_dict(path2)
    result = []
    plus = "+"
    minus = "-"
    space = " "
    first_file_item = dict_1.items()
    second_file_item = dict_2.items()
    diff_items_1 = first_file_item - second_file_item
    for key, value in diff_items_1:
        result.append(f"{plus} {key}: {value}")
    diff_items_2 = second_file_item - first_file_item
    for key, value in diff_items_2:
        result.append(f"{minus} {key}: {value}")
    compare_items = first_file_item & second_file_item
    for key, value in compare_items:
        result.append(f"{space} {key}: {value}")
    second_index = 2  # фильтруем по второму индексу
    last_index = -1  # фильтруем до последнего индекса
    result.sort(key=lambda by_name: by_name[second_index:last_index])
    new_result = ""
    for i in result:
        new_result = f"{new_result} {i}\n"
    print(new_result)
    return f"{{\n{new_result}}}"

