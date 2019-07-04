# -*- coding: utf-8 -*-


def isBadVersion(n):
    return n >= 4


class Solution:
    def firstBadVersion(self, n):
        if n == 0:
            return 0

        left, right, result, is_bad = 1, n, n, False
        while left <= right:
            middle = int((left + right) / 2)
            if isBadVersion(middle) is False:
                left = middle + 1
            else:
                is_bad = True
                right = middle - 1
                if middle < result:
                    result = middle

        return result if is_bad else 0
