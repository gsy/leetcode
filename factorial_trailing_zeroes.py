# -*- coding: utf-8 -*-

import math

class Solution:
    def trailingZeroes(self, n):
        times = int(sum(math.log10(i) for i in range(1, n+1)))
        num = 1
        for i in range(1, n + 1):
            num = num * i

        result = 0
        for i in range(times):
            if num % 10 == 0:
                result = result + 1
            num = int(num / 10)
        return result

if __name__ == "__main__":
    s = Solution()
    r = s.trailingZeroes(3)
    assert r == 0

    r = s.trailingZeroes(5)
    assert r == 1

    r = s.trailingZeroes(10)
    assert r == 2
