# -*- coding: utf-8 -*-


class Solution:
    def rotate(self, nums, k):
        length = len(nums)
        tmp = nums[:]
        for index, num in enumerate(nums):
            new_index = (index + k) % length
            nums[new_index] = tmp[index]

        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.rotate([1, 2, 3, 4, 5, 6, 7], k=3)

    s.rotate([-1, -100, 3, 99], k=2)
