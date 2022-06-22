import unittest
from numberToWord import Solution

class numberToWordTest(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution(3), 'Three')

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution(58), 'Fifty Eight')

    def test_3(self):
        solution = Solution()
        self.assertEqual(solution(1994), 'One Thousand Nine Hundred Ninety Four')

    def test_4(self):
        solution = Solution()
        self.assertEqual(solution(0), 'Zero')

    def test_5(self):
        solution = Solution()
        self.assertEqual(solution(1234567), 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven')


if __name__ == '__main__':
    unittest.main()
