__author__ = 'guang'

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        >>> s = Solution()
        >>> s.mySqrt(3)
        1
        >>> s.mySqrt(4)
        2
        >>> s.mySqrt(5)
        2
        >>> s.mySqrt(10)
        3
        >>> s.mySqrt(36)
        6
        """
        left, right = 1, x
        middle = (left + right) / 2
        while right - left > 1:
            square = middle * middle
            if square < x:
                left = middle
            elif square == x:
                break
            else:
                right = middle
            middle = (left + right) / 2

        return middle
