# -*- coding: utf-8 -*-


class Solution:
    def find132pattern(self, nums):
        if len(nums) == 0:
            return False

        maximum = None
        minimum = None
        up, down = False, False
        spans = []
        for i in range(len(nums)):
            print(f"i {i}, spans {spans}, maximum {maximum}, minimum {minimum}")
            for minimum, maximum in spans:
                return nums[i] > minimum and nums[i] < maximum

            if minimum is None:
                minimum = nums[i]
            elif nums[i] <= minimum:
                minimum = nums[i]
            if nums[i] > minimum:
                up = True

            if up:
                if maximum is None or nums[i] >= maximum:
                    maximum = nums[i]
                if nums[i] < maximum:
                    if (nums[i] in (minimum, maximum)):
                        return True
                    down = True

            if up and down and minimum is not None and maximum is not None:
                spans.append((minimum, maximum))
                up = False
                down = False
                minimum = None
                maximum = None

        return False
