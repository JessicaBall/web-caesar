def alphabet_position(letter):
    #takes an argument of a single letter
    #converts it to lower case
    #searches in the alphabet string and returns index position
    char_list = "abcdefghijklmnopqrstuvwxyz"
    return char_list.find(letter.lower())


def rotate_character(char,rot):
    #takes two arguments: character and rotation amount
    #determines if character is a letter, skips function if not
    #calls alphabet_position function to convert to int
    #changes position of index by number of rotation(rot)
    #returns character at new position
    char_list = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        char_num = alphabet_position(char) + rot
        if char_num > 25:
            char_num = char_num % 26
        new_letter = char_list[char_num]

        if char.isupper():
            return new_letter.upper()

        else:
            return new_letter

    else:
        return char

def encrypt(char, rot):
    rt_list = list(char)
    rot = int(rot)

    new_string = ""
    for i in (rt_list):
        new_string = new_string + rotate_character(i,rot)
    return new_string
