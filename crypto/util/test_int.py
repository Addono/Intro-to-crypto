from unittest import TestCase

from crypto.util.int import ext_gcd


class TestExt_gcd(TestCase):
    def test_ext_gcd(self):
        self.assertEqual(ext_gcd(3, 7), {'d': 1, 'x': -2, 'y': 1})
        self.assertEqual(ext_gcd(67, 140), {'d': 1, 'x': 23, 'y': -11})
