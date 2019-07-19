# -*- coding: utf-8 -*-


class Solution:
    def findLUSlength(self, a, b):
        length1, length2 = len(a), len(b)
        # b 是比较短的
        if length1 < length2:
            length1, length2 = length2, length1
            a, b = b, a

        matrix = [[0] * length2] * length2
        result = 0
        return result
