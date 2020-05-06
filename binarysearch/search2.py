class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1
