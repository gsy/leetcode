# -*- coding: utf-8 -*-


class Solution:
    def findMin(self, nums):
        length = len(nums)
        if length == 0:
            return None

        left, right = 0, length - 1
        if nums[right] > nums[left]:
            return nums[left]

        mini = nums[left]
        while(left <= right):
            middle = int((left + right) / 2)
            if (nums[middle] < nums[0]):
                right = middle - 1
                if nums[middle] < mini:
                    mini = nums[middle]
            else:
                left = middle + 1

        return min(mini, nums[0], nums[middle])


if __name__ == '__main__':
    s = Solution()
    r = s.findMin([4, 5, 6, 7, 0, 1, 2])
    print(r)
    assert r == 0

    r = s.findMin([5, 6, 7, 0, 1, 2, 4])
    assert r == 0

    r = s.findMin([6, 7, 0, 1, 2, 4, 5])
    assert r == 0

    r = s.findMin([7, 0, 1, 2, 4, 5, 6])
    assert r == 0

    r = s.findMin([0, 1, 2, 4, 5, 6, 7])
    assert r == 0

    r = s.findMin([1, 2, 4, 5, 6, 7, 0])
    assert r == 0

    r = s.findMin([2, 4, 5, 6, 7, 0, 1])
    assert r == 0

    r = s.findMin([4, 5, 6, 7, 0, 1, 2])
    assert r == 0

    r = s.findMin([4, 5, 6, 7, 0, 1, 2])
    assert r == 0

    r = s.findMin([4, 6, 7, 0, 1, 2])
    assert r == 0

    r = s.findMin([4, 7, 0, 1, 2])
    assert r == 0

    r = s.findMin([7, 0, 1, 2])
    assert r == 0

    r = s.findMin([0, 1, 2])
    assert r == 0

    r = s.findMin([1, 2])
    assert r == 1

    r = s.findMin([1])
    assert r == 1
