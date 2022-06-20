import unittest
from RomanToInt import Solution

class romanToIntTest(unittest.TestCase):
    def test_1(self):
        solution = Solution('III')
        self.assertEqual(solution(), 3)

    def test_2(self):
        solution = Solution('LVIII')
        self.assertEqual(solution(), 58)

    def test_3(self):
        solution = Solution('MCMXCIV')
        self.assertEqual(solution(), 1994)

    def test_4(self):
        solution = Solution('MCIV')
        self.assertEqual(solution(), 1104)


if __name__ == '__main__':
    unittest.main()
