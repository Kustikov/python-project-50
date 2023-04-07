#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.modules.parser import path1, path2


def main():
    generate_diff(path1, path2)


if __name__ == "__main__":
    main()
