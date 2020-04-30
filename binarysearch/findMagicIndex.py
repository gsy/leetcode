class Solution:
    def findMagicIndex(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[left] == left:
                return left

            elif nums[mid] == mid:
                right = mid
            else:
                left = left + 1

        return -1
