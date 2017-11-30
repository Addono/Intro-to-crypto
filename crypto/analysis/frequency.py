from collections import Counter


def text(data):
    c = Counter(data)
    print(c.most_common())