#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_tru = list(a_dictionary.keys())
    list_tru.sort()
    for i in list_tru:
        print("{}: {}".format(i, a_dictionary.get(i)))
