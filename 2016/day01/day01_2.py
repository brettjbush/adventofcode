#!/usr/bin/python
"""
--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""

import sys

def main():

    filename = sys.argv[1]

    forward = 1
    right = 1

    found_double = False

    x = 0
    y = 0

    file = open(filename)
    contents = file.read()
    print(contents)
    instructions = contents.split(", ")
    visited = list()
    visited.append([x, y])
    for instruction in instructions:

        turn = instruction[0]
        length = int(instruction[1:])
        print(length)
        if turn == 'R':
            old_forward = forward
            forward = right
            right = -old_forward
        else:
            old_forward = forward
            forward = -right
            right = old_forward
        if forward != right:
            for i in range(length):
                x += forward * 1
                if [x, y] in visited:
                    found_double = True
                    break
                visited.append([x, y])
        else:
            for i in range(length):
                y += forward * 1
                if [x, y] in visited:
                    found_double = True
                    break
                visited.append([x, y])
        if found_double:
            break
    if found_double:
        total = abs(x) + abs(y)
        print("Easter Bunny HQ is " + str(total) + " blocks away")
    else:
        print("Easter Bunny HQ can't be found! No double spots!")

if __name__ == "__main__":
    main()
