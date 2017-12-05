from unittest import TestCase

from crypto.cyphers.RC4 import RC4


class TestRC4(TestCase):
    test = {
        "Key" : ["EB", "9F", "77", "81", "B7", "34", "CA", "72", "A7", "19"],
        "Wiki": ["60", "44", "DB", "6D", "41", "B7"],
        "Secret": ["04", "D4", "6B", "05", "3C", "A8", "7B", "59"],
        "Passw" : ["D9", "05", "46", "66", "AB"],
        "P\x17*{ê": ['82', 'BD', 'FE', 'C0', 'EE', '84', 'D8', '84', '52', 'AD'] # HW1 exercise 3 key
    }

    def convert_key(self, key: list):
        if type(key[0]) is str:
            return [ord(char) for char in key]
        else:
            return key

    # def test_swap(self):
    #     self.fail()
    #
    def test_generate(self):
        for key, output in self.test.items():
            key = self.convert_key(key)

            rc4 = RC4(key)
            for c in output:
                result = rc4.generate()
                self.assertEqual(format(result, '02X'), str.upper(c))

    def test_generate_multiple(self):
        for key, output in self.test.items():
            key = self.convert_key(key)

            rc4_1 = RC4(key)
            rc4_2 = RC4(key)

            amount = len(output)
            output_1 = rc4_1.generate_multiple(amount)
            output_2 = rc4_2.generate_multiple(amount)

            self.assertEqual(output_1, output_2)

    # def test_get_s_index(self):
    #     self.fail()
