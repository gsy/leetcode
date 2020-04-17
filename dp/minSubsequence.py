class Solution:
    def minSubsequence(self, nums):
        result = []
        nums = sorted(nums, reverse=True)
        total = sum(nums)

        tmp = 0
        for num in nums:
            result.append(num)
            tmp = tmp + num
            if tmp > total - tmp:
                break

        return result
