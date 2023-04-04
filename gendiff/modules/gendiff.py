import json


def generate_diff(path1, path2):
    result = ""
    with open(f"{path1}", "r", encoding="utf-8") as f1:
        file_1 = json.load(f1)
    with open(f"{path2}", "r", encoding="utf-8") as f2:
        file_2 = json.load(f2)
    for key in sorted(file_1):
        if (key in file_2) and (file_1[key] == file_2[key]):
            result = f"{result} {key}: {file_1[key]}\n"
        elif (key in file_2) and (file_1[key] != file_2[key]):
            result = f"{result}-{key}: {file_1[key]}\n+{key}: {file_2[key]}\n"
        elif key not in file_2:
            result = f"{result}-{key}: {file_1[key]}\n"
    diff_items_2 = file_2.items() - file_1.items()
    for key, value in diff_items_2:
        result = f"{result}+{key}: {value}\n"
    print(f'{{\n{result}\n}}')
    return f'{{\n{result}\n}}'
