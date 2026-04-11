#!/usr/bin/python3
for i in range(26):
    if chr(ord('a') + i) != 'q' and chr(ord('a') + i) != 'e':
        print("{}".format(chr(ord('a') + i)), end="")
