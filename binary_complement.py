# -*- coding: utf-8 -*-


class Solution:
    def bitwiseComplement(self, n):
        # a + _a + 1 = 2^N
        if n == 0:
            return 1

        total = 1
        number = n
        while number > 0:
            number = number >> 1
            total = total << 1
        # print(f"total {total}")
        return (total - n - 1)
