import crypto.util.char as s


def ceasar_encrypt(string, key):
    result = ""
    for c in string:
        result += s.shiftChar(c, key)

    return result


def ceasar_decrypt(string, key):
    return ceasar_encrypt(string, -key)


def ceasar_decrypt_all(string):
    for c in range(0, 26):
        print str(c) + ": " + ceasar_decrypt(string, c)
