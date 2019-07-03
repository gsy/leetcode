# -*- coding: utf-8 -*-


class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        a, b = 1, 2
        for i in range(2, n):
            b, a = b + a, b

        return b
