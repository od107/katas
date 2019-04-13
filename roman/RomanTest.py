import unittest
from Roman import *


class RomanTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual('I', numeral2Roman(1))

    def test_3(self):
        self.assertEqual('III', numeral2Roman(3))

    def test_3123(self):
        self.assertEqual('MMMCXXIII', numeral2Roman(3123))

    def test_555(self):
        self.assertEqual('DLV', numeral2Roman(555))

    def test_678(self):
        self.assertEqual('DCLXXVIII', numeral2Roman(678))

    def test_444(self):
        self.assertEqual('CDXLIV', numeral2Roman(444))

    def test_999(self):
        self.assertEqual('CMXCIX', numeral2Roman(999))

    def test_1987(self):
        self.assertEqual('MCMLXXXVII', numeral2Roman(1987))

    def test_I(self):
        self.assertEqual(1, roman2Numeral('I'))

    def test_III(self):
        self.assertEqual(3, roman2Numeral('III'))

    def test_MMMCXXIII(self):
        self.assertEqual(3123, roman2Numeral('MMMCXXIII'))

    def test_DLV(self):
        self.assertEqual(555, roman2Numeral('DLV'))

    def test_DCLXXVIII(self):
        self.assertEqual(678, roman2Numeral('DCLXXVIII'))

    def test_CDXLIV(self):
        self.assertEqual(444, roman2Numeral('CDXLIV'))

    def test_CMXCIX(self):
        self.assertEqual(999, roman2Numeral('CMXCIX'))

    def test_MCMLXXXVII(self):
        self.assertEqual(1987, roman2Numeral('MCMLXXXVII'))


if __name__ == '__main__':
    unittest.main()
