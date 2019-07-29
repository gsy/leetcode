# -*- coding: utf-8 -*-

class Solution:
    def convert(self, digit):
        if digit == 0:
            return 'Z'
        return chr(ord('A') + (digit-1))

    def convertToTitle(self, n):
        # 26 进制，从1开始计数, Z是0
        digits = []
        while n > 0:
            digit = n % 26
            if digit == 0:
                n = n - 26
            n = int(n / 26)
            digits.append(self.convert(digit))

        # print(digits)
        return "".join(digits[::-1])

if __name__ == "__main__":
    s = Solution()
    r = s.convertToTitle(1)
    assert r == "A"

    r = s.convertToTitle(26)
    assert r == "Z"

    r = s.convertToTitle(27)
    print(r)
    assert r == "AA"

    r = s.convertToTitle(28)
    assert r == "AB"

    r = s.convertToTitle(701)
    print(r)
    assert r == "ZY"
