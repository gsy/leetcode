# -*- coding: utf-8 -*-


class Solution(object):
    def search(self, nums, target):
        length = len(nums)
        if length == 0:
            return -1

        # 两个队列是升序的，合并到了一起, 后边的一截肯定是值比较小的
        left, right = 0, length - 1

        while left <= right:
            middle = int((left + right) / 2)
            if nums[middle] == target:
                return middle
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            elif nums[middle] > target:
                if nums[left] < nums[middle]:
                    # (break, middle)
                    if target >= nums[left]:
                        right = middle - 1
                    else:
                        left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[left] > nums[middle]:
                    # 向左找可能更好
                    if target >= nums[left]:
                        right = middle - 1
                    else:
                        left = middle + 1
                else:
                    left = middle + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    r = s.search([], 0)
    assert r == -1

    r = s.search([1, 3], 3)
    assert r == 1

    r = s.search([5, 1, 2, 3, 4], 1)
    assert r == 1

    r = s.search([1], 0)
    assert r == -1

    r = s.search([1], 1)
    assert r == 0

    r = s.search([1, 0], 0)
    assert r == 1

    r = s.search([1, 0], 1)
    assert r == 0

    r = s.search([1, 0], 2)
    assert r == -1

    r = s.search([4, 5, 6, 7, 0, 1, 2], 2)
    assert r == 6

    r = s.search([4, 5, 6, 7, 0, 1, 2], 4)
    assert r == 0

    r = s.search([4, 5, 6, 7, 0, 1, 2], 5)
    assert r == 1

    r = s.search([4, 5, 6, 7, 0, 1, 2], 6)
    assert r == 2

    r = s.search([4, 5, 6, 7, 8, 1, 2, 3], 8)
    assert r == 4

    r = s.search([4, 5, 6, 7, 8, 1, 2, 3], 7)
    assert r == 3

    r = s.search([4, 5, 6, 7, 8, 1, 2, 3], 1)
    assert r == 5

    r = s.search([4, 5, 6, 7, 8, 1, 2, 3], 2)
    assert r == 6
