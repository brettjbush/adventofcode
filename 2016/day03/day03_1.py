#!/usr/bin/python
"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""

import sys

def main():

    filename = sys.argv[1]

    valid_triangle_count = 0

    file = open(filename)
    contents = file.read()
    print(contents)
    side_sets = contents.splitlines()
    for side_set in side_sets:
        invalid_found = False
        sides = list()
        for side_string in side_set.split():
            sides.append(int(side_string))
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
