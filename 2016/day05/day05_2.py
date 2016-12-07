#!/usr/bin/python
"""
--- Part Two ---

As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also indicates the position within the password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character represents the position (0-7), and the seventh character is the character to put in that position.

A hash result of 000001f means that f is the second character in the password. Use only the first result for each position, and ignore invalid positions.

For example, if the Door ID is abc:

The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8).
The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.
You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.

Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a cinematic "decrypting" animation.
"""

import sys
import md5

def main():

    filename = sys.argv[1]

    password_string_list = ["","","","","","","",""]
    password_string_found = [False,False,False,False,False,False,False,False]

    file = open(filename)
    door_id = file.read().splitlines()[0]
    complete = False

    num = 0
    num_found = 0
    while not complete:
        md5_hash = md5.new()
        hash_string = door_id + str(num)
        md5_hash.update(hash_string)
        hex_string = md5_hash.hexdigest()
        if hex_string.startswith("00000"):
            location_string = hex_string[5]
            if location_string.isdigit():
                location = int(location_string)
                if location < 8:
                    if not password_string_found[location]:
                        character = hex_string[6]
                        password_string_list[location] = character
                        password_string_found[location] = True
                        num_found += 1
                        if(num_found == 8):
                            complete = True
        num += 1

    password_string = "".join(password_string_list)
    print(password_string)

if __name__ == "__main__":
    main()
