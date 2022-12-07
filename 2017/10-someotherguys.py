"""From https://raw.githubusercontent.com/HenRuKey/AdventOfCode/master/Day%2010/knot_hash.py"""
from itertools import cycle


def get_lengths(file_name="lengths.txt"):
    lengths_file = open(file_name)
    lengths = lengths_file.readline().split(',')
    return lengths


def get_hash_list(array_size=256):
    hash_list = []
    for value in range(array_size):
        hash_list.append(value)
    return hash_list


def get_apply_sublist(hash_list, hash_index, selection_range):
    selection = []
    index = hash_index
    for i in range(selection_range):
        if index >= len(hash_list):
            index = 0
        selection.append(hash_list[index])
        index += 1
    selection.reverse()
    for select in selection:
        if hash_index >= len(hash_list):
            hash_index = 0
        hash_list[hash_index] = select
        hash_index += 1
    return hash_list


def manipulate_hash(lengths, hash_list):
    hash_index = 0
    skip_size = 0
    for index in range(len(lengths)):
        if hash_index >= len(hash_list):
            hash_index = hash_index % len(hash_list)
        length = int(lengths[index])
        hash_list = get_apply_sublist(hash_list, hash_index, length)
        hash_index += length + skip_size
        skip_size += 1


def main():
    lengths = get_lengths()
    hash_list = get_hash_list()
    manipulate_hash(lengths, hash_list)
    print("Product: " + str(hash_list[0] * hash_list[1]))


if __name__ == "__main__":
    main()