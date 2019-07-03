# -*- coding: utf-8 -*-


class Solution:
    def searchInsert(self, nums, target):
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return 0 if nums[0] >= target else 1
        else:
            left, right = 0, length-1
            while True:
                middle = int((left + right) / 2)
                if left >= right:
                    break
                if left + 1 == right:
                    if target > nums[right]:
                        return right + 1
                    elif target > nums[left]:
                        return right
                    elif target < nums[left]:
                        return left - 1
                    else:
                        return left

                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
            return middle
