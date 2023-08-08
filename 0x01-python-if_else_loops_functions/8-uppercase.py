#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_val = ord(char)
        if ascii_val >= ord('a') and ascii_val <= ord('z'):
            print("{}".format(chr(ascii_val - 32)), end="")
        else:
            print("{}".format(char), end="")
