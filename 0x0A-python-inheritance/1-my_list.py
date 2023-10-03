#!/usr/bin/python3
"""
This module defines a custom list class, MyList.
"""

class MyList(list):
    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
