class Solution:
    def missingNumber(self, nums):
        total, N = 0, len(nums)
        for num in nums:
            total = total + num

        return (N * (N + 1)) // 2 - total
