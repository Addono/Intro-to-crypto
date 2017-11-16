import unittest
from crypto.util.char import addChar


def testAdd(self, a, b, r):
    c = addChar(a, b)  # The computed result
    self.assertEqual(c, r)  # Check if it coincides with the expected result


class TestChar(unittest.TestCase):
    def test_addChar(self):
        testAdd(self, 'a', 'c', 'c')
        testAdd(self, 'd', 'p', 's')
        testAdd(self, 'b', 'o', 'p')


if __name__ == '__main__':
    unittest.main()
