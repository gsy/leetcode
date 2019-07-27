# -*- coding: utf-8 -*-


class Solution:
    def containsDuplicate(self, nums):
        prev = {}
        for num in nums:
            if num in prev:
                return True
            else:
                prev[num] = 1
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.containsDuplicate([1, 2, 3, 1])
    assert r is True

    r = s.containsDuplicate([1, 2, 3, 4])
    assert r is False

    r = s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    assert r is True
