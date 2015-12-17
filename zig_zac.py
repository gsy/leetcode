__author__ = 'guang'
# coding: utf-8

class Solution(object):
    def zig(self, start, stop, step, s):
        """
        first and last row string.
        :param start:
        :param stop:
        :param step:
        :param s:
        :return:
        >>> s = Solution()
        >>> text = "PAYPALISHIRING"
        >>> s.zig(0, len(text), 4, text)
        'PAHN'
        >>> s.zig(2, len(text), 4, text)
        'YIR'
        """
        indexs = range(start, stop, step)
        return ''.join([s[index] for index in indexs])

    def zag(self, start, stop, numRows, s):
        """
        :param start:
        :param stop:
        :param step:
        :param s:
        :return:
        >>> s = Solution()
        >>> text = "ABCDE"
        >>> s.zag(2, len(text), 4, text)
        'CE'
        >>> s.zag(1, len(text), 4, text)
        'B'
        >>> text = "PAYPALISHIRING"
        >>> s.zag(1, len(text), 3, text)
        'APLSIIG'
        """
        step = 2 * numRows - 2
        start2 = start + 2 * (numRows - 1 - start)
        indexs = sorted(range(start, stop, step) + range(start2, stop, step))
        return ''.join([s[index] for index in indexs])

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        >>> text = "PAYPALISHIRING"
        >>> s = Solution()
        >>> s.convert(text, 3)
        'PAHNAPLSIIGYIR'
        >>> s.convert("", 2)
        ''
        >>> s.convert(text, 1)
        'PAYPALISHIRING'
        >>> s.convert('', 1)
        ''
        >>> s.convert("ABCDE", 4)
        'ABCED'
        """
        if numRows == 1:
            return s

        n = len(s)
        zig_step = 2 * numRows - 2

        result = ""
        result += self.zig(0, n, zig_step, s)
        for i in range(1, numRows-1):
            result += self.zag(i, n, numRows, s)
        result += self.zig(numRows-1, n, zig_step, s)

        return result