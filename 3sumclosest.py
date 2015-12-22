__author__ = 'guang'

class Solution(object):
    def closest(self, nums, target):
        """

        :param nums:
        :param target:
        :return:
        >>> s = Solution()
        >>> s.closest([-4, -1, 1, 2], 1)
        -1
        >>> s.closest([-1, 1, 2], 1)
        2
        >>> s.closest([0,1,2], 3)
        3
        """
        if len(nums) < 3:
            return 2147483647

        i, j, k, result, min_diff = 0, 1, len(nums) - 1, 2147483647, 2147483647

        x = nums[0]
        while j < k:
            y = nums[j]
            z = nums[k]
            sum = x + y + z
            if sum == target:
                return sum
            else:
                difference = abs(sum - target)
                if difference < min_diff:
                    min_diff = difference
                    result = sum
                if sum > target:
                    k -= 1
                elif sum < target:
                    j += 1
        return result

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        >>> s = Solution()
        >>> s.threeSumClosest([-1, 2, 1, -4], 1)
        2
        >>> s.threeSumClosest([], 10)
        0
        >>> s.threeSumClosest([4, 5], 10)
        9
        """
        if len(nums) < 3:
            sum = 0
            for x in nums:
                sum += x
            return sum

        result, min = 0, 2147483647
        nums = sorted(nums)
        for i in range(len(nums)):
            sum = self.closest(nums[i:], target)
            difference = abs(sum - target)
            if difference < min:
                min = difference
                result = sum

        return result



