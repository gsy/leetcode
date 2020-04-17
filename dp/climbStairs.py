# -*- coding: utf-8 -*-


class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 1, 2
            for i in range(2, n+1):
                a, b = b, a + b

            return a
