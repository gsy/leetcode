# -*- coding: utf-8 -*-


class Solution:
    def minSteps(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 2

        for j in range(n-1, 2, -1):
            # print("j", j)
            if n % j == 0:
                times = int(n / j)
                # print("times", times)
                return (1 + (times - 1) + self.minSteps(j))

        return n
