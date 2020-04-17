__author__ = 'guang'

def isBadVersion(version):
        if version in [2,4,5,7,9]:
            return True
        else:
            return False


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        >>> s = Solution()
        >>> s.firstBadVersion(1)
        0
        >>> s.firstBadVersion(3)
        2
        >>> s.firstBadVersion(2)
        2
        """
        if n < 1:
            return n

        left, right = 1, n
        while left < right:
            middle = (left + right) / 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1

        if isBadVersion(left):
            return left

        return 0



