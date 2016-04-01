__author__ = 'guang'

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        >>> s = Solution()
        >>> s.searchRange([], 1)
        [-1, -1]
        >>> s.searchRange([1], 1)
        [0, 0]
        >>> s.searchRange([1, 1], 1)
        [0, 1]
        >>> s.searchRange([1, 1, 1, 1], 1)
        [0, 3]
        >>> s.searchRange([1, 2, 2, 3], 2)
        [1, 2]
        >>> s.searchRange([5, 7, 7, 8, 8, 10], 8)
        [3, 4]
        >>> s.searchRange([5, 7, 7, 8, 8, 10, 12], 12)
        [6, 6]
        >>> s.searchRange([5, 7, 7, 8, 8, 10, 12], 5)
        [0, 0]
        """
        length = len(nums)
        if length < 1:
            return [-1, -1]
        elif length == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        left, right = 0, length - 1
        while left <= right:
            if nums[left] == target and nums[right] == target:
                return [left, right]

            index = (left + right) / 2
            middle = nums[index]
            if middle < target:
                left = index + 1
            elif middle > target:
                right = index - 1
            else:
                left = index
                right = index
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < length and nums[right] == target:
                    right += 1

                return [left + 1, right - 1]

        return [-1, -1]















