#!/usr/bin/env python3
from gendiff import generate_diff, get_dict
from gendiff.modules.parser import path1, path2


def main():
    dict_1 = get_dict(path1)
    dict_2 = get_dict(path2)
    generate_diff(dict_1, dict_2)


if __name__ == "__main__":
    main()
