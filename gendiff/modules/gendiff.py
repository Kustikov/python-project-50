import json


def generate_diff(path1, path2):
    print(path1)
    print(path2)
    with open(f"{path1}", "r", encoding="utf-8") as f1:
        file_1 = json.load(f1)
    print(file_1)
    with open(f"{path2}", "r", encoding="utf-8") as f2:
        file_2 = json.load(f2)
    print(file_2)