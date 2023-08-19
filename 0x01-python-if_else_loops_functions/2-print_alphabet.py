#!/usr/bin/python3

output = ""
for n in range(0, 26):
    output += "{}".format(chr(ord('a') + n))

print(output, end="")
