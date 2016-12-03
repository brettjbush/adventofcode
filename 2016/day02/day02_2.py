#!/usr/bin/python
"""
--- Part Two ---

You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D
You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

You start at "5" and don't move at all (up and left are both edges), ending at 5.
Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?
"""

import sys

def clamp(x, low_bound, high_bound):
    return max(low_bound, min(x, high_bound))

def main():

    filename = sys.argv[1]

    row_low_bound = 0
    row_high_bound = 4

    col_low_bound = 0
    col_high_bound = 4

    row = 2
    col = 2

    sequence = list()

    file = open(filename)
    contents = file.read()
    print(contents)
    instructions = contents.splitlines()
    for instruction in instructions:
        for direction in list(instruction):
            if direction == 'U' :
                row = clamp(row - 1, row_low_bound, row_high_bound)
                col_low_bound = abs(row - 2)
                col_high_bound = 4 - abs(row - 2)
            elif direction == 'R':
                col = clamp(col + 1, col_low_bound, col_high_bound)
                row_low_bound = abs(col - 2)
                row_high_bound = 4 - abs(col - 2)
            elif direction == 'D':
                row = clamp(row + 1, row_low_bound, row_high_bound)
                col_low_bound = abs(row - 2)
                col_high_bound = 4 - abs(row - 2)
            else:
                col = clamp(col - 1, col_low_bound, col_high_bound)
                row_low_bound = abs(col - 2)
                row_high_bound = 4 - abs(col - 2)
        counter = 0
        for num in range(0,row):
            counter += 4 - abs(num - 2) - abs(num - 2) + 1
        key_number = counter + 1 + col - abs(row - 2)
        character = ""
        if key_number < 10:
            character = str(key_number)
        elif key_number == 10:
            character = "A"
        elif key_number == 11:
            character = "B"
        elif key_number == 12:
            character = "C"
        elif key_number == 13:
            character = "D"
        sequence.append(character)

    code = "".join(sequence)
    print("The bathroom code is: " + code)

if __name__ == "__main__":
    main()
