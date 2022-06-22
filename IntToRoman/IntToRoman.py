
class Solution:
    def __init__(self, num: int):
        self.num = num

    @staticmethod
    def IntToRoman(self) -> str:
        result = ''

        lookup = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]

        for (n, roman) in lookup:
            div = self.num // n
            self.num %= n
            while div:
                result += roman
                div -= 1

        print(result)
        return result

    def __call__(self, *args, **kwargs):
        return self.IntToRoman(self)


if __name__ == '__main__':
    solution = Solution(1994)
    solution()
