# -*- coding: utf-8 -*-


class Solution:
    def is_palindrome(self, s, start, end):
        length = end - start
        if length == 0:
            return True

        half = int(length / 2)
        if length % 2 == 0:
            left_start, left_end, right_start, right_end = start, start + half - 1, start + half, end
        else:
            left_start, left_end, right_start, right_end = start, start + half - 1, start + half + 1, end

        i, j = left_start, right_end
        while i <= j and i <= left_end and j >= right_start:
            if s[i] != s[j]:
                return False
            else:
                i, j = i + 1, j - 1
        return True

    def longestPalindrome(self, s):
        length = len(s)
        if length == 0:
            return ""

        if length % 2 == 0:
            pass
