__author__ = 'guang'


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        >>> s = Solution()
        >>> s.intToRoman(0)
        ''
        >>> s.intToRoman(3)
        'III'
        >>> s.intToRoman(14)
        'XIV'
        >>> s.intToRoman(578)
        'DLXXVIII'
        >>> s.intToRoman(2909)
        'MMCMIX'
        """
        romanNumeral = {}
        romanNumeral['ones'] = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        romanNumeral['tens'] = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        romanNumeral['hundreds'] = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        romanNumeral['thousands'] = ['', 'M', 'MM', 'MMM', 'MMMM', 'MMMMM', 'MMMMMM', 'MMMMMMM', 'MMMMMMMM', 'MMMMMMMMM']

        ones = num % 10
        tens = (num / 10) % 10
        hundreds = (num / 100) % 10
        thousands = (num / 1000) % 10

        result = romanNumeral['thousands'][thousands] + romanNumeral['hundreds'][hundreds] + \
        romanNumeral['tens'][tens] + romanNumeral['ones'][ones]

        return result.lstrip()
