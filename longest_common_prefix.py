__author__ = 'guang'

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        >>> s = Solution()
        >>> s.longestCommonPrefix(["", ""])
        ''
        >>> s.longestCommonPrefix(["a", ""])
        ''
        >>> s.longestCommonPrefix([""])
        ''
        >>> s.longestCommonPrefix(["a", "ab", "abcd"])
        'a'
        >>> s.longestCommonPrefix(["abc", "ad", "bcd"])
        ''
        >>> s.longestCommonPrefix(["bcd", "abc", "ad"])
        ''
        >>> s.longestCommonPrefix(["abcd", "bcdf", "ab", "b"])
        ''
        >>> s.longestCommonPrefix(["bcdf", "b"])
        'b'
        >>> s.longestCommonPrefix(["a"])
        'a'
        >>> s.longestCommonPrefix(["a", "a", "b"])
        ''
        """

        if len(strs) == 0:
            return ''

        length = 0
        x = strs[0]
        for i in range(len(x)):
            match = True
            for y in strs[1:]:
                if i < len(y) and x[i] == y[i]:
                    continue
                else:
                    match = False
                    break
            if match:
                length += 1
            else:
                break

        return x[:length]
