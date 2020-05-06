class Solution:
    def minSubArrayLen(self, s, nums):
        i, j = 0, 0
        acc = 0
        length = len(nums)
        result = length + 1
        while j < length:
            acc += nums[j]
            j += 1
            if acc >= s:
                while acc - nums[i] >= s and i < j:
                    acc -= nums[i]
                    i = i + 1

                # print("i", i, "j", j, "acc", acc)
                if (j - i) < result:
                    result = j - i

        return 0 if result == length + 1 else result
