__author__ = 'guang'

import sys
class Solution(object):
    def even(self, number):
        return number & 0x1 == 0x0

    def odd(self, number):
        return number & 0x1 == 0x1

    def divide2(self, number):
        return number >> 1

    def multiple2(self, number):
        return number << 1

    def abs_divide(self, dividend, divisor):
        """
        >>> s = Solution()
        >>> s.abs_divide(10, 3)
        (3, 1)
        >>> s.abs_divide(3, 2)
        (1, 1)
        >>> s.abs_divide(6, 2)
        (3, 0)
        >>> s.abs_divide(12, 2)
        (6, 0)
        >>> s.abs_divide(25, 2)
        (12, 1)
        >>> s.abs_divide(1021989372, 82778243)
        (12, 28650456)
        """
        if divisor == 0:
            return sys.maxint

        if divisor == 1:
            return dividend, 0

        if dividend < divisor:
            return 0, dividend
        elif dividend == divisor:
            return 1, 0

        if self.even(dividend) and self.even(divisor):
            a, b = self.abs_divide(self.divide2(dividend), self.divide2(divisor))
            return a, self.multiple2(b)
        elif self.odd(dividend) and self.even(divisor):
            a, b = self.abs_divide(dividend - 1, divisor)
            if b + 1 == divisor:
                return a + 1, 0
            else:
                return a, b + 1
        elif self.even(dividend) and self.odd(divisor):
            a, b = self.abs_divide(dividend, divisor + 1)
            c, d = self.abs_divide(a + b, divisor)
            return a + c, d
        else:
            a, b = self.abs_divide(dividend - 1, divisor + 1)
            c, d = self.abs_divide(a + b + 1, divisor)
            return a + c, d

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        >>> s = Solution()
        >>> s.divide(10, 3)
        3
        >>> s.divide(-10, 0)
        -2147483648
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
        >>> s.divide(-2147483648, -3)
        715827882
        >>> s.divide(2147483647, 3)
        715827882
        >>> s.divide(-1021989372, -82778243)
        12
        >>> s.divide(-2147483648, -1)
        2147483647
        """
        maxInt = 2147483647
        minInt = -2147483648

        if dividend == 0:
            return 0
        elif divisor == 0:
            if dividend > 0:
                return maxInt
            else:
                return minInt

        if dividend > 0 and divisor > 0:
            result = self.abs_divide(dividend, divisor)[0]
        elif dividend > 0 and divisor < 0:
            result = -(self.abs_divide(dividend, 0 - divisor)[0])
        elif dividend < 0 and divisor > 0:
            result = -(self.abs_divide(0 - dividend, divisor)[0])
        else:
            result = self.abs_divide(0 - dividend, 0 - divisor)[0]

        if result < minInt:
            return minInt
        elif result > maxInt:
            return maxInt
        else:
            return result






