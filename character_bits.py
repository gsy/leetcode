# -*- coding: utf-8 -*-


class Solution:
    def isOneBitCharacter(self, bits):
        if len(bits) == 0:
            return False

        start, end = 0, len(bits)
        while start < end:
            if bits[start] == 1:
                step = 2
                start = start + step
            else:
                step = 1
                start = start + step
        return step == 1
