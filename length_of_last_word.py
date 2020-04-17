# -*- coding: utf-8 -*-


class Solution:
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return 0

        words = s.split()
        if len(words) == 0:
            return 0

        return len(words[-1])
