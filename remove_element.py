__author__ = 'guang'

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        >>> s = Solution()
        >>> s.removeElement([], 1)
        0
        >>> s.removeElement([1], 1)
        0
        >>> s.removeElement([1], 2)
        1
        >>> s.removeElement([1,2,3], 1)
        2
        >>> s.removeElement([4,5], 4)
        1
        """
        for x in nums[:]:
            if x == val:
                nums.remove(x)

        return len(nums)


