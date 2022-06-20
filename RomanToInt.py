# convert Roman numbers to Integer
class Solution:
    def __init__(self, s: str):
        self.s = s

    @staticmethod
    def romanToInt(self) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        s = self.s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace(
            "CD", "CCCC").replace("CM", "DCCCC")

        for digit in s:
            num += roman[digit]

        return num

    def __call__(self, *args, **kwargs):
        return self.romanToInt(self)


# if __name__ == '__main__':
#     solution = Solution('MCMXCIV')
#     solution()
