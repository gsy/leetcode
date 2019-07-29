# -*- coding: utf-8 -*-


class Solution:
    def findMaxLength(self, nums):
        left, right, length = 0, 0, len(nums)
        # 滑动窗口，左边不动，右边一直往前移动
        # 滑动过程中可以记下当前下标下0和１的个数和
        # zeros, ones 是总数，那么　result <= min(zeros, ones)
        # 连续是什么意思？ left和right之间
        # left 什么时候调整？


        result, zeros, ones = 0, 0, 0
        while right < length:
            if nums[right] == 0:
                zeros = zeros + 1
            else:
                ones = ones + 1
