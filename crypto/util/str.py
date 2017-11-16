from crypto.util.char import to_int


def frequency_distribution(string):
    count = frequency_count(string)

    return [float(value) / len(string) for value in count]


def frequency_count(string):
    # Create an array with keys being all lower case characters
    result = []
    for i in range(26):
        result.append(0)

    # Increment for each character
    for char in string.lower():
        i = to_int(char)

        if 0 <= i < 26:
            result[i] += 1

    return result


def alternating_string_split(string, length):
    result = []
    for _ in range(length):
        result.append('')

    i = 0
    for char in string:
        result[i] += char
        i = (i + 1) % length

    return result
