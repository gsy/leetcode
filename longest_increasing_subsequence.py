__author__ = 'guang'

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> s = Solution()
        >>> s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
        4
        >>> s.lengthOfLIS([1])
        1
        >>> s.lengthOfLIS([])
        0
        >>> s.lengthOfLIS([1, 2])
        2
        >>> s.lengthOfLIS([2, 1])
        1
        >>> s.lengthOfLIS([1, 2, 3])
        3
        >>> s.lengthOfLIS([1, 3, 2])
        2
        >>> s.lengthOfLIS([1,3,6,7,9,4,10,5,6])
        6
        """
        length = len(nums)
        if length < 1:
            return length

        p = [1] * length

        for i in range(1, length):
            num = nums[i]
            best = 0
            for j in range(i, -1, -1):
                if num > nums[j] and p[j] > best:
                    best = p[j]

            p[i] += best

        return max(p)






