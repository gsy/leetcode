# -*- coding: utf-8 -*-


class Solution:
    def binary_search(self, nums, start, end, target):
        if start > end:
            return -1
        elif start == end:
            if (nums[start] == target):
                return start
            else:
                return -1
        else:
            middle = start + int((end - start) / 2)
            # print(f"middle {middle}")
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                return self.binary_search(nums, start, middle-1, target)
            else:
                return self.binary_search(nums, middle+1, end, target)

    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0

        return self.binary_search(nums, 0, len(nums) - 1, target)
