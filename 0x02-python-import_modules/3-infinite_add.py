#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total_sum = sum(int(arg) for arg in argv[1:])
    print(total_sum)
