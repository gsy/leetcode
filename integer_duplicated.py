__author__ = 'guang'

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        >>> s = Solution()
        >>> s.containsDuplicate([1, 2, 3])
        False
        >>> s.containsDuplicate([1, 1, 2, 3])
        True
        >>> s.containsDuplicate([])
        False
        """

        unique = set(nums)

        return len(unique) != len(nums)


