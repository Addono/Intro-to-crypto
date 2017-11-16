from crypto.util.char import addChar, subChar


def vigenere_encrypt(string, key):
    i = 0  # Tracks the index of the upcoming evaluated character of the key.
    result = ''  # Stores the intermediate result.

    for char in string:
        result += addChar(char, key[i])
        i = (i + 1) % len(key)

    return result


def vigenere_decrypt(string, key):
    i = 0
    result = ''

    for char in string:
        result += subChar(char, key[i])
        i = (i + 1) % len(key)

    return result
