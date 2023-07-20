#!/usr/bin/env python3
from gendiff import generate_diff, get_dict, change_type
from gendiff.modules.parser import path1, path2


def main():
    dict_1 = get_dict(path1)
    dict_2 = get_dict(path2)
    data = generate_diff(change_type(dict_1), change_type(dict_2))
    print(data)
    # """ diff = stylish(data)
    # print(diff) """


if __name__ == "__main__":
    main()
