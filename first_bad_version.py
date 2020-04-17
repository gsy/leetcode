<<<<<<< HEAD
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



=======
# -*- coding: utf-8 -*-


def isBadVersion(n):
    return n >= 4


class Solution:
    def firstBadVersion(self, n):
        if n == 0:
            return 0

        left, right, result, is_bad = 1, n, n, False
        while left <= right:
            middle = int((left + right) / 2)
            if isBadVersion(middle) is False:
                left = middle + 1
            else:
                is_bad = True
                right = middle - 1
                if middle < result:
                    result = middle

        return result if is_bad else 0
>>>>>>> af85e649bb30ac65699bc91d8c414c7905d2f668
