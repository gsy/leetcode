__author__ = 'guang'

class Solution(object):
    def removeInPlace(self, nums):
        """
        :param nums:
        :return:
        :type nums: List[int]
        :rtype: int

        >>> s = Solution()
        >>> nums = [1,1,2]
        >>> s.removeInPlace(nums)
        >>> nums
        [1, 2]
        >>> nums = [1,1,1,2,3]
        >>> s.removeInPlace(nums)
        >>> nums
        [1, 2, 3]
        >>> nums = [1,1,2,2,2,3]
        >>> s.removeInPlace(nums)
        >>> nums
        [1, 2, 3]
        """
        if len(nums) <= 1:
            return

        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                nums.remove(nums[index])
            else:
                index += 1

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> s = Solution()
        >>> nums = [1,1,2]
        >>> s.removeDuplicates(nums)
        2
        >>> nums = [1,1,1,2,3]
        >>> s.removeDuplicates(nums)
        3
        >>> s.removeDuplicates([1,1,2,2,3])
        3
        """
        self.removeInPlace(nums)
        return len(nums)
