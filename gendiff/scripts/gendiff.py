#!/usr/bin/env python3

import argparse

def gendiff():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')

    # Positional arguments
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    args = parser.parse_args()
    return args.first_file, args.second_file


def main():
    gendiff()


if __name__ == '__main__':
    main()
