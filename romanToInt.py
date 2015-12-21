__author__ = 'guang'

class Solution(object):
    def __init__(self):
        self.romanNumeral = {}
        self.romanNumeral.update({'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000})

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        >>> s = Solution()
        >>> s.romanToInt("III")
        3
        >>> s.romanToInt("IV")
        4
        >>> s.romanToInt("VII")
        7
        >>> s.romanToInt("CCLVI")
        256
        """
        if s == '':
            return 0

        x = self.romanNumeral[s[0]]
        if len(s) > 1:
            y = self.romanNumeral[s[1]]
            if x < y:
                return (y-x) + self.romanToInt(s[2:])

        return x + self.romanToInt(s[1:])


