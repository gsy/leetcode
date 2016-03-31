__author__ = 'guang'

class Solution(object):
    def max_index_2(self, nums, i, j):
        if nums[i] > nums[j]:
            return i
        else:
            return j

    def max_index_3(self, nums, i, j, k):
        if nums[i] > nums[j]:
            return self.max_index_2(nums, i, k)
        else:
            return self.max_index_2(nums, j, k)

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> s = Solution()
        >>> s.findPeakElement([1, 2, 3, 1])
        2
        >>> s.findPeakElement([1, 2])
        1
        >>> s.findPeakElement([1])
        0
        >>> s.findPeakElement([1, 2, 3])
        2
        >>> s.findPeakElement([1, 2, 3, 4])
        3
        >>> s.findPeakElement([3, 2, 1])
        0
        >>> s.findPeakElement([4, 3, 2, 1])
        0
        >>> s.findPeakElement([1, 3, 2])
        1
        >>> s.findPeakElement([1, 4, 3, 2])
        1
        >>> s.findPeakElement([1, 5, 6, 4, 3, 2])
        2
        >>> s.findPeakElement([1, 5, 6, 4, 3, 10])
        2
        >>> s.findPeakElement([1, 5, 6, 7, 4, 3, 10])
        3
        >>> s.findPeakElement([1, 5, 6, 7, 8, 3, 10])
        6
        >>> s.findPeakElement([1, 5, 6, 7, 8, 10, 3])
        5
        >>> s.findPeakElement([1,2,3,4,3])
        3
        """
        length = len(nums)
        if length < 2:
            return 0

        if length == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        left, right = 0, length - 1
        while left < right:
            middle = (left + right) / 2
            if right - left == 1:
                return self.max_index_2(nums, left, right)
            elif right - left == 2:
                return self.max_index_3(nums, left, left + 1, right)

            if nums[left] <= nums[middle] <= nums[right]:
                left = middle
            elif nums[left] >= nums[middle] >= nums[right]:
                right = middle
            elif nums[middle] >= nums[left] and nums[middle] >= nums[right]:
                left += 1
                right -= 1
            else:
                right = middle





