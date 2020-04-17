# -*- coding: utf-8 -*-


class Solution:
    def findErrorNums(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        repeat, lost = None, None
        for num in range(1, len(nums) + 1):
            if num not in count:
                lost = num
            elif count[num] > 1:
                repeat = num
        return [repeat, lost]


if __name__ == "__main__":
    s = Solution()
    r = s.findErrorNums([1, 2, 2, 4])
    assert r == [2, 3]
