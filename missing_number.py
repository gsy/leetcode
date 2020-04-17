# -*- coding: utf-8 -*-


class Solution:
    def missingNumber(self, nums):
        n, current = 0, 0
        for num in nums:
            n = n + 1
            current = current + num
        total = int(((1+n) * n) / 2)
        return total - current


if __name__ == "__main__":
    s = Solution()
    r = s.missingNumber([3, 0, 1])
    assert r == 2

    r = s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
    assert r == 8
