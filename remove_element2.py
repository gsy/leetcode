# -*- coding: utf-8 -*-

class Solution:
    def removeElement(self, nums, val):
        # move val to end of nums
        length = len(nums)
        if length == 0:
            return 0

        begin, end = 0, length - 1
        while begin <= end:
            while nums[end] == val and begin <= end:
                end = end - 1

            while nums[begin] != val and begin < end:
                begin = begin + 1

            if begin > end:
                break

            nums[begin], nums[end] = nums[end], nums[begin]
            begin = begin + 1
            end = end - 1

        return begin

if __name__ == "__main__":
    s = Solution()
    r = s.removeElement([], 10)
    assert r == 0

    r = s.removeElement([3, 2, 2, 3], 3)
    print(r)
    assert r == 2

    r = s.removeElement([3, 2, 3, 3], 3)
    print(r)
    assert r == 1

    r = s.removeElement([3, 3, 3, 3], 3)
    assert r == 0

    r = s.removeElement([2, 3, 3, 3, 3], 3)
    assert r == 1

    r = s.removeElement([3], 3)
    assert r == 0

    r = s.removeElement([2], 3)
    assert r == 1
