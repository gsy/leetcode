# -*- coding: utf-8 -*-

class Solution:
    def removeDuplicates(self, nums):
        # rewrite nums
        length = len(nums)
        if length == 0:
            return 0

        position, target = 0, None
        for index in range(length):
            if target is None:
                target = nums[index]
                position = position + 1
                continue
            else:
                if nums[index] == target:
                    continue
                else:
                    nums[position] = nums[index]
                    position = position + 1
                    target = nums[index]

        return position


if __name__ == "__main__":
    s = Solution()
    r = s.removeDuplicates([1, 1, 2])
    print(r)
    assert r == 2

    r = s.removeDuplicates([1, 1])
    print(r)
    assert r == 1

    r = s.removeDuplicates([])
    assert r == 0

    r = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    assert r == 5
