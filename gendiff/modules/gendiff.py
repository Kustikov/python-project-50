import json


def generate_diff(path1, path2):
    result = ""
    with open(f"{path1}", "r", encoding="utf-8") as f1:
        file_1 = json.load(f1)
    with open(f"{path2}", "r", encoding="utf-8") as f2:
        file_2 = json.load(f2)
    # for key in sorted(file_1):
    #     if (key in file_2) and (file_1[key] == file_2[key]):
    #         result = f"{result} {key}: {file_1[key]}\n"
    #     elif (key in file_2) and (file_1[key] != file_2[key]):
    #         result = f"{result}-{key}: {file_1[key]}\n+{key}: {file_2[key]}\n"
    #     elif key not in file_2:
    #         result = f"{result}-{key}: {file_1[key]}\n"
    # diff_items_2 = file_2.items() - file_1.items()
    # for key, value in diff_items_2:
    #     result = f"{result}+{key}: {value}\n"
    # print(f'{{\n{result}\n}}')
    # return f'{{\n{result}\n}}'
    result = []
    plus = "+"
    minus = "-"
    space = " "
    first_file_item = file_1.items()
    second_file_item = file_2.items()
    diff_items_1 = first_file_item - second_file_item
    for key, value in diff_items_1:
        result.append(f"{minus} {key}: {value}")
        # result = f'{result}- {key}: {value}\n'
    diff_items_2 = second_file_item - first_file_item
    for key, value in diff_items_2:
        result.append(f"{plus} {key}: {value}")
        # result = f'{result}+ {key}: {value}\n'
    compare_items = first_file_item & second_file_item
    for key, value in compare_items:
        result.append(f"{space} {key}: {value}")
        # result = f'{result}  {key}: {value}\n'
    second_index = 2  # фильтруем по второму индексу
    result.sort(key=lambda by_name: by_name[second_index])
    new_result = ""
    for i in result:
        new_result = f"{new_result} {i}\n"
    print((f"{{\n{new_result}\n}}"))
    return f"{{\n{new_result}\n}}"
