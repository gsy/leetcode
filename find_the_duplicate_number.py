__author__ = 'guang'

class Solution(object):
    def f(self, s, i):
        return s[i]

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> s = Solution()
        >>> s.findDuplicate([1, 2, 3, 1])
        1
        >>> s.findDuplicate([4, 1, 3, 1])
        1
        >>> s.findDuplicate([2, 3, 1, 1, 4, 5])
        1
        >>> s.findDuplicate([2, 3, 1, 4, 3, 5, 7, 6])
        3
        """
        length = len(nums)
        if length == 2:
            return nums[0]

        slow, fast = length, length
        while True:
            slow = nums[slow - 1]
            fast = nums[nums[fast - 1] - 1]
            if slow == fast:
                break

        finder = length
        while True:
            finder = nums[finder - 1]
            slow = nums[slow - 1]
            if finder == slow:
                return finder

        return 0


