#!/usr/bin/env python3
from gendiff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output", default="JSON")
    args = parser.parse_args()
    path1 = args.first_file
    path2 = args.second_file

    if args.format == "JSON":
        generate_diff(path1, path2)
    else:
        print("OOPS")


if __name__ == "__main__":
    main()
