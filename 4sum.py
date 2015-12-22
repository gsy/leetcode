__author__ = 'guang'

class Solution(object):
    def twoSum(self, nums, target):
        """

        :param nums:
        :param target:
        :return:
        >>> s = Solution()
        >>> s.twoSum([-2, -2, -2, -1, 0, 0 ,1], 0)
        [[-1, 1], [0, 0]]
        >>> s.twoSum([-2, -2, -2, -1, 0, 0 ,1], -2)
        [[-2, 0]]
        """
        if len(nums) < 2:
            return []

        i, j = 0, len(nums) - 1
        result = []
        unique_num = []
        while i < j:
            sum = nums[i] + nums[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                if nums[i] in unique_num:
                    i += 1
                else:
                    result.append([nums[i], nums[j]])
                    unique_num.append(nums[i])
                    i += 1
                    j -= 1

        return result

    def threeSum(self, nums, target):
        """

        :param nums:
        :param target:
        :return:
        >>> s = Solution()
        >>> s.threeSum([-1, 0, 0, 1, 2], 2)
        [[-1, 1, 2], [0, 0, 2]]
        >>> s.threeSum([-1,0,2,4], 5)
        [[-1, 2, 4]]
        >>> s.threeSum([-1,0,2,4], 3)
        [[-1, 0, 4]]
        >>> s.threeSum([-1, 0, 0, 1, 2], 2)
        [[-1, 1, 2], [0, 0, 2]]
        >>> s.threeSum([-4, -2, -2, -2, -1, 0, 0 ,1], -4)
        [[-4, -1, 1], [-4, 0, 0], [-2, -2, 0]]
        """
        if len(nums) < 3:
            return []

        result = []
        unique = []
        for i in range(len(nums) - 2):
            if nums[i] in unique:
                continue
            else:
                new_target = target - nums[i]
                pairs = self.twoSum(nums[i+1:], new_target)
                for pair in pairs:
                    sub = []
                    sub.append(nums[i])
                    sub.extend(pair)
                    result.append(sub)
                unique.append(nums[i])

        return result

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        >>> s = Solution()
        >>> s.fourSum([1, 0, -1, 0, -2, 2], 0)
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        >>> s.fourSum([], 0)
        []
        >>> s.fourSum([1,2,3], 6)
        []
        >>> s.fourSum([-3,-1,0,2,4,5], 2)
        [[-3, -1, 2, 4]]
        >>> s.fourSum([-3,-1,0,2,4,5], 0)
        [[-3, -1, 0, 4]]
        >>> s.fourSum([-3,-2,-1,0,0,1,2,3], 0)
        [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        >>> s.fourSum([-5,-4,-3,-2,-1,0,0,1,2,3,4,5], 0)
        [[-5, -4, 4, 5], [-5, -3, 3, 5], [-5, -2, 2, 5], [-5, -2, 3, 4], [-5, -1, 1, 5], [-5, -1, 2, 4], [-5, 0, 0, 5], [-5, 0, 1, 4], [-5, 0, 2, 3], [-4, -3, 2, 5], [-4, -3, 3, 4], [-4, -2, 1, 5], [-4, -2, 2, 4], [-4, -1, 0, 5], [-4, -1, 1, 4], [-4, -1, 2, 3], [-4, 0, 0, 4], [-4, 0, 1, 3], [-3, -2, 0, 5], [-3, -2, 1, 4], [-3, -2, 2, 3], [-3, -1, 0, 4], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        >>> s.fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9)
        [[-5, -4, -1, 1], [-5, -4, 0, 0], [-5, -2, -2, 0], [-4, -2, -2, -1]]
        """
        if len(nums) < 4:
            return []

        nums = sorted(nums)
        result = []
        unique = []
        for i in range(len(nums)-3):
            if nums[i] in unique:
                continue
            else:
                new_target = target - nums[i]
                pairs = self.threeSum(nums[i+1:], new_target)
                for pair in pairs:
                    sub = []
                    sub.append(nums[i])
                    sub.extend(pair)
                    result.append(sub)
                unique.append(nums[i])

        return result





