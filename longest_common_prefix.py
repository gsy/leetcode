__author__ = 'guang'

class Solution(object):
    def commonPrefix(self, s1, s2):
        if s1 == '' or s2 == '':
            return ''

        if s1[0] != s2[0]:
            return ''

        return s1[0] + self.commonPrefix(s1[1:], s2[1:])

    def longestStr(self, strs):
        lengths = map(len, strs)
        max = 0
        result = 0
        for i, length in enumerate(lengths):
            if length > max:
                max = length
                result = i

        return result

    def foo(self, strs):
        if len(strs) <= 1:
            return ''

        result = ''
        max = 0
        i = self.longestStr(strs)
        x = strs[i]
        new_strs = []
        for j in range(len(strs)):
            if j == i:
                continue
            y = strs[j]
            prefix = self.commonPrefix(x, y)
            length = len(prefix)
            if length == 0:
                new_strs.append(y)
            elif length > max:
                max = length
                result = prefix

        new_prefix = self.foo(new_strs)
        if len(result) > len(new_prefix):
            return result
        else:
            return new_prefix


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
        'ab'
        >>> s.longestCommonPrefix(["abc", "ad", "bcd"])
        'a'
        >>> s.longestCommonPrefix(["bcd", "abc", "ad"])
        'a'
        >>> s.longestCommonPrefix(["abcd", "bcdf", "ab", "b"])
        'ab'
        >>> s.longestCommonPrefix(["bcdf", "b"])
        'b'
        >>> s.longestCommonPrefix(["a"])
        'a'
        >>> s.longestCommonPrefix(["a", "a", "b"])
        ''
        """
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]

        return self.foo(strs)




