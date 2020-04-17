# -*- coding: utf-8 -*-


class Solution:
    def searchInsert(self, nums, target):
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return 0 if target <= nums[0] else 1
        else:
            left, right = 0, length - 1

            while left < right:
                middle = int((left + right) / 2)
                if nums[middle] == target:
                    return middle
                if target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
            if target <= nums[left]:
                return left

            return left + 1
