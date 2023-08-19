#!/usr/bin/python3
output = ""
for tens in range(10):
    for ones in range(tens + 1, 10):
        output += "{:02d}, ".format(tens * 10 + ones)

output = output[:-2]
print(output)
