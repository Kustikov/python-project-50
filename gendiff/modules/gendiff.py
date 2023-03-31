import json


def generate_diff(path1, path2):
    print(path1)
    print(path2)
    # Открываем файлы по полученному в скрипте PATH
    with open(f"{path1}", "r", encoding="utf-8") as f1:
        file_1 = json.load(f1)
    with open(f"{path2}", "r", encoding="utf-8") as f2:
        file_2 = json.load(f2)
    # Сортируем полученные dict по ключу в алфавитном порядке
    sorted_keys_1 = sorted(file_1.keys())
    sorted_keys_2 = sorted(file_2.keys())
    sorted_dict_1 = {}
    for i in sorted_keys_1:
        sorted_dict_1[i] = file_1[i]
    sorted_dict_2 = {}
    for i in sorted_keys_2:
        sorted_dict_2[i] = file_2[i]
    print(sorted_dict_1)
    print(sorted_dict_2)
