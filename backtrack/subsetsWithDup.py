class Solution:
    def backtrack(self, nums, start, end, path, result):
        result.append(path)

        for i in range(start, end):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.backtrack(nums, i + 1, end, path + [nums[i]], result)

    def subsetsWithDup(self, nums):
        end = len(nums)
        path, result = [], []
        nums = sorted(nums)
        self.backtrack(nums, 0, end, path, result)
        return result
