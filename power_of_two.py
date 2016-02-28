class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        >>> s = Solution()
        >>> s.isPowerOfTwo(3)
        False
        >>> s.isPowerOfTwo(4)
        True
        >>> s.isPowerOfTwo(8)
        True
        >>> s.isPowerOfTwo(10)
        False
        """
        if n == 1:
            return True

        guess = 2
        while guess <= n:
            if n ^ guess == 0:
                return True
            else:
                guess <<= 1

        return False


