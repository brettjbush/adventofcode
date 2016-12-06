#!/usr/bin/python
"""
--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
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
    
    decoded_entries = list()

    file = open(filename)
    contents = file.read()
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
        for character_info in character_info_list[:5]:
            result = result + character_info.character

        if result == checksum:
            offset = sector_id % 26
            encoded_string = room_name[:room_name.rfind("-")].replace("-", " ")
            decoded_string = ""
            for character in list(encoded_string):
                if character == " ":
                    decoded_string = decoded_string + " "
                else:
                    new_character = chr((ord(character) - 97 + offset) % 26 + 97)
                    decoded_string = decoded_string + new_character
            decoded_entries.append(decoded_string + ": " + str(sector_id))
           
    for decoded_entry in decoded_entries:
        if "north" in decoded_entry:
            print(decoded_entry)

if __name__ == "__main__":
    main()
