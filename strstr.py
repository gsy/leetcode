__author__ = 'guang'

import string

class Solution(object):
    def sundayInitocc(self, p):
        result = {}

        for i in string.ascii_letters:
            result[i] = -1

        for i in range(len(p)):
            result[p[i]] = i

        return result

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        >>> s = Solution()
        >>> s.strStr("hello", "he")
        0
        >>> s.strStr("hello", "world")
        -1
        >>> s.strStr("he", "")
        0
        >>> s.strStr("", "")
        0
        >>> s.strStr("world", "worldwide")
        -1
        >>> s.strStr("mississippi", "issip")
        4
        """

        haystack_length = len(haystack)
        needle_length = len(needle)
        if needle_length == 0:
            return 0

        i = 0
        occurance = self.sundayInitocc(needle)
        while i <= haystack_length - needle_length:
            j = 0
            save = i
            while i < haystack_length and j < needle_length and haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == needle_length:
                    return save

            # mismatch
            end = save + needle_length
            if end < haystack_length:
                wanted = haystack[end]
                if wanted in occurance:
                    i = end - occurance[wanted]
                else:
                    i = end + 1
            else:
                break

        return -1
