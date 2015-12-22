__author__ = 'guang'

class Solution(object):
    def firstZeroPosition(self, nums):
        """

        :param nums:
        :return:
        >>> s = Solution()
        >>> s.firstZeroPosition([3, 2, 0])
        2
        >>> s.firstZeroPosition([0])
        0
        >>> s.firstZeroPosition([1,2,3])
        3
        """
        result = 0
        for x in nums:
            if x != 0:
                result += 1
            else:
                break

        return result



    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        >>> s = Solution()
        >>> nums = [0, 1, 0, 3, 12]
        >>> s.moveZeroes(nums)
        >>> nums
        [1, 3, 12, 0, 0]
        >>> nums = [0, 0, 0]
        >>> s.moveZeroes(nums)
        >>> nums
        [0, 0, 0]
        >>> nums = [1, 3, 0, 5, 0, 10, 0, 0, 50]
        >>> s.moveZeroes(nums)
        >>> nums
        [1, 3, 5, 10, 50, 0, 0, 0, 0]
        >>> nums = [0]
        >>> s.moveZeroes(nums)
        >>> nums
        [0]
        """

        if len(nums) == 0:
            return

        length = len(nums)
        j = self.firstZeroPosition(nums)
        if j >= length - 1:
            return

        i = j + 1
        while i < length:
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            else:
                i += 1





