# -*- coding: utf-8 -*-


class Solution:
    def searchRange(self, nums, target):
        length = len(nums)
        if length == 0:
            return [-1, -1]

        left, right, begin, end = 0, length-1, -1, -1
        while left <= right:
            middle = int((left + right) / 2)
            if nums[middle] == target:
                # 在 (left, right) 之间寻找开头和结尾
                for i in range(left, right + 1):
                    if nums[i] == target:
                        if begin < 0:
                            begin = i
                        end = i
                break

            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return [begin, end]


if __name__ == '__main__':
    s = Solution()
    r = s.searchRange([], 1)
    assert r == [-1, -1]
    r = s.searchRange([1], 1)
    assert r == [0, 0]
    r = s.searchRange([1, 1], 1)
    assert r == [0, 1]

    r = s.searchRange([1, 1, 1, 1], 1)
    assert r == [0, 3]
    r = s.searchRange([1, 2, 2, 3], 2)
    assert r == [1, 2]

    r = s.searchRange([5, 7, 7, 8, 8, 10], 8)
    assert r == [3, 4]
    r = s.searchRange([5, 7, 7, 8, 8, 10, 12], 12)
    assert r == [6, 6]
    r = s.searchRange([5, 7, 7, 8, 8, 10, 12], 5)
    assert r == [0, 0]
