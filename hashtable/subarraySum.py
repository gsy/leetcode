class Solution:
    def subarraySum(self, nums, k):
        length = len(nums)

        acc = 0
        result = 0
        sums = {0: 1}
        for i in range(length):
            acc = acc + nums[i]
            if (acc - k) in sums:
                result += sums[acc - k]
            sums[acc] = sums.get(acc, 0) + 1

        return result
