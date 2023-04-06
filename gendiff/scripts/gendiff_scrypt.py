#!/usr/bin/env python3
from gendiff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", help="set format of output",
                        default="JSON")
    args = parser.parse_args()
    path1 = args.first_file
    path2 = args.second_file
    print(path1)
    print(path2)
    if args.format == "JSON":
        generate_diff(path1, path2)
    else:
        print("OOPS")


if __name__ == "__main__":
    main()
