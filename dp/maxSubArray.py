# -*- coding: utf-8 -*-


class Solution:
    def maxSubArray(self, nums):
        length = len(nums)
        if length == 0:
            return 0

        if length == 1:
            return nums[0]

        local_max = None
        last = None
        result = None
        for i, num in enumerate(nums):
            if i == 0:
                local_max = nums[i]
                last = max(nums[i], 0)
                result = local_max
            else:
                if last > 0:
                    local_max = nums[i] + last
                else:
                    local_max = nums[i]
                last = local_max
                if local_max > result:
                    result = local_max
        return result
