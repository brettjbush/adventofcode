#!/usr/bin/python
"""
--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
"""

import sys

def main():

    filename = sys.argv[1]

    valid_triangle_count = 0

    block_height = 3
    block_width = 3

    file = open(filename)
    contents = file.read()
    print(contents)
    side_sets = contents.splitlines()
    blocks = list()
    for i in range(len(side_sets) / block_height):
        block = list()
        for i in range(block_height):
            block.append(side_sets.pop(0).split())
        blocks.append(block)
    for block in blocks:
        for col in range(block_width):
            sides = list()
            for row in range(block_height):
                sides.append(int(block[row][col]))
            invalid_found = False
            for i in range(len(sides)):
                sides_temp = list(sides)
                comp_val = sides_temp.pop(i)
                sides_sum = sum(sides_temp)
                if sides_sum <= comp_val:
                    invalid_found = True
                    break
            if not invalid_found:
                valid_triangle_count += 1

    print("There are " + str(valid_triangle_count) + " possible triangles in the list")

if __name__ == "__main__":
    main()
