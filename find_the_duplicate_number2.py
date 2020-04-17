# -*- coding: utf-8 -*-


class Solution:
    def less_than(self, nums, middle):
        less, equal = 0, 0
        for item in nums:
            if item < middle:
                less = less + 1
            elif item == middle:
                equal = equal + 1
        return less, equal

    def findDuplicate(self, nums):
        length = len(nums)
        if length <= 1:
            return None

        left, right = 1, length - 1
        while left <= right:
            middle = int((left + right) / 2)
            less, equal = self.less_than(nums, middle)

            if less >= middle:
                right = middle - 1
            else:
                if equal > 1:
                    return middle
                else:
                    left = middle + 1

        return middle


if __name__ == '__main__':
    s = Solution()
    r = s.findDuplicate([1, 3, 4, 2, 2])
    print(r)
    assert r == 2

    r = s.findDuplicate([1, 3, 2, 2])
    assert r == 2

    r = s.findDuplicate([1, 3, 2, 4, 4])
    assert r == 4

    r = s.findDuplicate([1, 3, 2, 4, 4, 5])
    assert r == 4

    r = s.findDuplicate([1, 3, 6, 2, 4, 4, 5])
    print(r)
    assert r == 4

    r = s.findDuplicate([1, 3, 6, 2, 4, 4, 4, 5])
    assert r == 4

    r = s.findDuplicate([1, 3, 6, 2, 4, 5, 6])
    assert r == 6
