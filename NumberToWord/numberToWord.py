# using recursion
class Solution:
    def numberToWords(self, num: int) -> str:
        ans = ""
        d = {
            1000000000: 'Billion',
            1000000: 'Million',
            1000: 'Thousand',
            100: 'Hundred',
            90: 'Ninety',
            80: 'Eighty',
            70: 'Seventy',
            60: 'Sixty',
            50: 'Fifty',
            40: 'Forty',
            30: 'Thirty',
            20: 'Twenty',
            19: 'Nineteen',
            18: 'Eighteen',
            17: 'Seventeen',
            16: 'Sixteen',
            15: 'Fifteen',
            14: 'Fourteen',
            13: 'Thirteen',
            12: 'Twelve',
            11: 'Eleven',
            10: 'Ten',
            9: 'Nine',
            8: 'Eight',
            7: 'Seven',
            6: 'Six',
            5: 'Five',
            4: 'Four',
            3: 'Three',
            2: 'Two',
            1: 'One'}

        if num == 0:
            return 'Zero'
        for n, word in d.items():
            x = num // n
            if x:
                if n >= 100:  # We say "One Hundred", "One thousand" but we don't say "One Fifty", we simply say "Fifty
                    ans += self.numberToWords(x) + ' '
                ans += word + " "
                num = num % n  # preparing the number for next loop
        print(ans.strip())
        return ans.strip()

    def __call__(self, num):
        return self.numberToWords(num)


if __name__ == '__main__':
    solution = Solution()
    solution(1234567)


# example:
# n= 1000000,   x1=1,   num=234567
# n= 1000,      x2=234, num=567
# n= 100,       x3=5,   num=67
# n=60,       x4=1,   num=7
# n=7,        x5=1,   num=0
