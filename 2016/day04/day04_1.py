#!/usr/bin/python
"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""

import sys

class CharacterInfo:

    def __init__(self, character, amount):
        self.character = character
        self.amount = amount
        
    def __lt__(self, other):
        if self.amount == other.amount:
            return self.character < other.character
        else:
            return self.amount > other.amount

def main():

    filename = sys.argv[1]
    
    sector_ids = list()

    file = open(filename)
    contents = file.read()
    print(contents)
    room_names = contents.splitlines()
    for room_name in room_names:
        entry_elements = room_name.split("-")
        sector_id_checksum_block = entry_elements.pop()
        sector_id_checksum_block_split = sector_id_checksum_block.split("[")
        sector_id = int(sector_id_checksum_block_split[0])
        checksum = sector_id_checksum_block_split[1][:-1]
        
        name_character_list = list("".join(entry_elements))
        
        character_info_list = list()
        for character in set(name_character_list):
            character_info_list.append(CharacterInfo(character, name_character_list.count(character)))
            
        character_info_list.sort()
        
        result = ""
        for character in character_info_list[:5]:
            result = result + character.character

        if result == checksum:
            sector_ids.append(sector_id)

    print("The sum of the valid sector ids is " + str(sum(sector_ids)))

if __name__ == "__main__":
    main()
