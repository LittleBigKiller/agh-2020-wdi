import unittest
from zad_01 import is_positive_int, nwd_euclid


class TestPosInt(unittest.TestCase):

    def test_posint_true(self):
        self.assertTrue(is_positive_int(3))

    def test_posint_zero(self):
        self.assertFalse(is_positive_int(0))

    def test_posint_negative(self):
        self.assertFalse(is_positive_int(-2))

    def test_posint_intlike(self):
        self.assertTrue(is_positive_int("2"))

    def test_posint_str(self):
        self.assertFalse(is_positive_int("a"))

    def test_posint_float(self):
        self.assertFalse(is_positive_int(0.02))


class TestNwd(unittest.TestCase):

    def test_nwd_agtb(self):
        self.assertEqual(nwd_euclid(5000, 50), 50)

    def test_nwd_altb(self):
        self.assertEqual(nwd_euclid(165, 304), 1)

    def test_nwd_aeqb(self):
        self.assertEqual(nwd_euclid(20, 20), 20)

    def test_nwd_one(self):
        self.assertEqual(nwd_euclid(2310, 13), 1)

    def test_nwd_notone(self):
        self.assertEqual(nwd_euclid(150, 9), 3)


if __name__ == '__main__':
    unittest.main()
