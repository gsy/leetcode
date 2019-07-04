__author__ = 'guang'


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        >>> s = Solution()
        >>> s.searchInsert([1,3,5,6], 5)
        2
        >>> s.searchInsert([1,3,5,6], 2)
        1
        >>> s.searchInsert([1,3,5,6], 7)
        4
        >>> s.searchInsert([1,3,5,6], 0)
        0
        >>> s.searchInsert([1,3,5,6], 6)
        3
        >>> s.searchInsert([1,3,5,6,10], 9)
        4
        >>> s.searchInsert([1,3,5,6,10], 4)
        2
        >>> s.searchInsert([1,3,5,6,10], 10)
        4
        >>> s.searchInsert([1,3,5,6,10], 1)
        0
        >>> s.searchInsert([3,5,6,10], 1)
        0
        >>> s.searchInsert([3,5,6,10], 3)
        0
        """
        length = len(nums)
        if length == 0:
            return 0

        left, right = 0, length - 1

        while left < right:
            middle = (left + right) / 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        if target <= nums[left]:
            return left
        else:
            return left + 1
