#!/usr/bin/env
# coding: utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int


        >>> s = Solution()
        >>> s.lengthOfLongestSubstring("")
        0
        >>> s.lengthOfLongestSubstring("a")
        1
        >>> s.lengthOfLongestSubstring("bb")
        1
        >>> s.lengthOfLongestSubstring("ab")
        2
        >>> s.lengthOfLongestSubstring("abcabcbb")
        3
        >>> s.lengthOfLongestSubstring("bbbb")
        1
        >>> s.lengthOfLongestSubstring("abba")
        2
        >>> s.lengthOfLongestSubstring("qwnfenpglqdq")
        8
        """

        already_scan = {}
        left = 0
        result = 0
        for current, x in enumerate(s):
            if x not in already_scan:
                already_scan[x] = current
            else:
                if already_scan[x] >= left:
                    length = current - left
                    result = max(result, length)
                    left = already_scan[x] + 1
                already_scan[x] = current

        result = max(result, len(s) - left)
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()


