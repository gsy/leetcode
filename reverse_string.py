# -*- coding: utf-8 -*-


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        if length <= 1:
            return

        start, end = 0, len(s) - 1
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
        print(s)


if __name__ == '__main__':
    s = Solution()
    s.reverseString(['h', 'e', 'l', 'l', 'o'])

    s.reverseString(['h'])

    s.reverseString(['h', 'e'])

    s.reverseString(["H","a","n","n","a","h"])
