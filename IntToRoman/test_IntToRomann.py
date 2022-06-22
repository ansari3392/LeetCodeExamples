import unittest
from IntToRoman import Solution

class IntToRomanTest(unittest.TestCase):
    def test_1(self):
        solution = Solution(3)
        self.assertEqual(solution(), 'III')

    def test_2(self):
        solution = Solution(58)
        self.assertEqual(solution(), 'LVIII')

    def test_3(self):
        solution = Solution(1994)
        self.assertEqual(solution(), 'MCMXCIV')

    def test_4(self):
        solution = Solution(1104)
        self.assertEqual(solution(), 'MCIV')

    def test_5(self):
        solution = Solution(3549)
        self.assertEqual(solution(), 'MMMDXLIX')


if __name__ == '__main__':
    unittest.main()
