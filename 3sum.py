__author__ = 'guang'

class Solution(object):
    def pairs(self, nums):
        """

        :param nums:
        :return:
        >>> s = Solution()
        >>> s.pairs([-5, -4, -1, 0, 1, 3, 7])
        []
        >>> s.pairs([-4, -1, 0, 1, 3, 7])
        [(-4, 1, 3)]
        >>> s.pairs([-1, 0, 1, 3, 7])
        [(-1, 0, 1)]
        >>> s.pairs([0, 1, 3, 7])
        []
        """
        if len(nums) < 3:
            return []

        if nums[0] * nums[-1] > 0:
            return []

        j, k = 1, len(nums)-1
        x = nums[0]
        target = x * -1
        result = []
        already_calculate = []
        while j < k:
            y = nums[j]
            z = nums[k]
            sum = y + z
            if sum > target:
                k -= 1
            elif sum < target:
                j += 1
            else:
                if y in already_calculate:
                    j += 1
                else:
                    result.append((x, y, z))
                    already_calculate.append(y)
                    j += 1
                    k -= 1
        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        >>> s = Solution()
        >>> s.threeSum([])
        []
        >>> s.threeSum([1,3])
        []
        >>> s.threeSum([1,-1, 5])
        []
        >>> s.threeSum([1, -1, 0])
        [(-1, 0, 1)]
        >>> s.threeSum([-4, -2, 0, 0, 0, 2, 4])
        [(-4, 0, 4), (-2, 0, 2), (0, 0, 0)]
        >>> s.threeSum([-1, 0, 1, 2, -1, -4])
        [(-1, -1, 2), (-1, 0, 1)]
        >>> s.threeSum([-2,0,0,2,2])
        [(-2, 0, 2)]
        """
        result = []
        nums = sorted(nums)
        already_calculate = []
        for i in range(len(nums)):
            if nums[i] in already_calculate:
                continue
            else:
                pairs = self.pairs(nums[i:])
                result.extend(pairs)
                already_calculate.append(nums[i])

        return result

