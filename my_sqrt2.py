# -*- coding: utf-8 -*-


class Solution(object):
    def mySqrt(self, x):
        if x <= 3:
            return 1

        left, right = 1, x
        while left <= right:
            middle = int((left + right) / 2)
            target = middle * middle
            if target == x:
                return middle
            elif target > x:
                # (1, 8) -> (1，4) -> (3, 4) -> (3)
                right = middle - 1
            else:
                left = middle + 1

        return middle
