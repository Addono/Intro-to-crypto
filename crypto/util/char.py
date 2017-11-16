def shiftChar(char, shift):
    i = to_int(char)

    if i < 0 or i > 25:
        # Character is not a letter, skip it
        return char

    i = (i + shift) % 26

    return to_char(i)


def addChar(char1, char2):
    i1 = to_int(char1)
    i2 = to_int(char2)

    if i1 < 0 or i2 < 0 or i1 > 25 or i2 > 25:
        raise ValueError('Both letters should be lower case characters')

    return shiftChar(char1, i2)


def subChar(char1, char2):
    i1 = to_int(char1)
    i2 = to_int(char2)

    if i1 < 0 or i2 < 0 or i1 > 25 or i2 > 25:
        raise ValueError('Both letters should be lower case characters')

    return shiftChar(char1, -i2)


def to_int(char):
    return ord(char) - 97


def to_char(i):
    return chr(i + 97)
