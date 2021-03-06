__author__ = 'guang'

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> s = Solution()
        >>> s.findMin([])
        0
        >>> s.findMin([4, 4, 5, 6, 7, 0, 1, 2])
        0
        >>> s.findMin([4, 5, 5, 5, 5, 5, 6, 7, 1, 2])
        1
        >>> s.findMin([4, 5, 6, 7, 13, 1, 2, 3])
        1
        >>> s.findMin([2, 1])
        1
        >>> s.findMin([1, 2])
        1
        >>> s.findMin([2, 1, 1, 1])
        1
        >>> s.findMin([2, 2, 2, 1, 1, 1])
        1
        >>> s.findMin([2, 2, 2, 3, 1, 1, 1])
        1
        >>> s.findMin([2, 3, 1])
        1
        >>> s.findMin([3, 1, 2])
        1
        >>> s.findMin([2, 3, 1])
        1
        >>> s.findMin([3, 1, 3])
        1
        >>> s.findMin([3, 3, 1, 3])
        1
        >>> s.findMin([10,1,10,10,10])
        1
        >>> s.findMin([3,3,3,3,1,1])
        1
        >>> s.findMin([1,1,1])
        1
        >>> s.findMin([1,1,1,2])
        1
        >>> s.findMin([1,1,1,2,1,1])
        1
        >>> s.findMin([1,1,2,1,1])
        1
        """
        length = len(nums)
        if length < 1:
            return 0

        left, right = 0, length - 1

        while left < right:
            index = (left + right) / 2
            middle = nums[index]
            if middle == nums[left] == nums[right]:
                left += 1
                right -= 1
            elif middle <= nums[right] < nums[left] or middle < nums[right] <= nums[left]:
                right = index
            elif nums[right] < nums[left] <= middle or nums[right] <= nums[left] < middle:
                left = index + 1
            else:
                return nums[left]

        return nums[left]

