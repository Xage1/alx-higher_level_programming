#!/usr/bin/python3

for tens in range(10):
    for ones in range(tens + 1, 10):
        if tens < 9:
            print("{:02d}, ".format(tens * 10 + ones), end="")
        else:
            print("{:02d}".format(tens * 10 + ones), end="")
