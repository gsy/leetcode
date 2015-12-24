__author__ = 'guang'

import sys
class Solution(object):
    def divide_ignore_sign(self, dividend, divisor):
        if divisor == 0:
            return sys.maxint

        if dividend < divisor:
            return 0
        elif dividend == divisor:
            return 1

        result = 0
        while True:
            remain = dividend - divisor
            result += 1
            dividend = remain
            if dividend < divisor:
                break

        return result

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        >>> s = Solution()
        >>> s.divide(10, 3)
        3
        >>> s.divide(-10, 0)
        -9223372036854775807
        >>> s.divide(1, 2)
        0
        >>> s.divide(100, 2)
        50
        >>> s.divide(3, -1)
        -3
        >>> s.divide(-3, -1)
        3
        >>> s.divide(-3, 1)
        -3
        >>> s.divide(3, 1)
        3
        >>> s.divide(0, 1)
        0
        >>> s.divide(-2147483648, -1)
        2147483648
        """
        if dividend == 0:
            return 0
        elif divisor == 0:
            if dividend > 0:
                return sys.maxint
            else:
                return 0 - sys.maxint

        if dividend > 0 and divisor > 0:
            return self.divide_ignore_sign(dividend, divisor)
        elif dividend > 0 and divisor < 0:
            return 0 - self.divide_ignore_sign(dividend, 0 - divisor)
        elif dividend < 0 and divisor > 0:
            return 0 - self.divide_ignore_sign(0 - dividend, divisor)
        else:
            return self.divide_ignore_sign(0 - dividend, 0 - divisor)





