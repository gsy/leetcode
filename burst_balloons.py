# -*- coding: utf-8 -*-


class Solution:
    def min_num_indexes(self, nums):
        minimum = min(nums)
        result = []
        for index, num in enumerate(nums):
            if num == minimum:
                result.append(index)
        return result

    def calculate_coins(self, nums, index):
        left = nums[index - 1] if index >= 1 else 1
        right = nums[index + 1] if index < len(nums)-1 else 1
        return left * nums[index] * right

    def maxCoins(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] * nums[1] + max(nums)
        elif len(nums) == 3:
            return (nums[1] * nums[0] * nums[2]) + self.maxCoins([nums[0], nums[2]])

        indexes = self.min_num_indexes(nums)
        choose = None
        best_result = None
        for index in indexes:
            result = self.calculate_coins(nums, index)
            if best_result is None:
                best_result = result
                choose = index
            elif best_result < result:
                best_result = result
                choose = index

        copy = [value for i, value in enumerate(nums) if i != choose]
        return best_result + self.maxCoins(copy)
