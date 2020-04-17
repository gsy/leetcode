# -*- coding: utf-8 -*-

class Solution:
    def majorityElement(self, nums):
        count = {}
        length = len(nums)
        for num in nums:
            result = count.get(num, 0) + 1
            count[num] = result
            if result > int(length / 2):
                return num

if __name__ == "__main__":
    s = Solution()
    r = s.majorityElement([3, 2, 3])
    assert r == 3

    r = s.majorityElement([2, 2, 1, 1, 1])
    assert r == 1

    r = s.majorityElement([2, 2, 1, 1, 1, 2, 2])
    assert r == 2
