class Solution:
    def backtrack(self, nums, start, end, path, result):
        result.append(path)

        for i in range(start, end):
            # path = path + [nums[i]]
            # self.backtrack(nums, i+1, end, path, result)
            # path = path[:-1]
            self.backtrack(nums, i+1, end, path + [nums[i]], result)

    def subsets(self, nums):
        def backtrack(start, path):
            result.append(path)

            for i in range(start, end):
                backtrack(i + 1, path + [nums[i]])

        path, result = [], []
        end = len(nums)
        # backtrack(0, path)
        self.backtrack(nums, 0, end, path, result)

        return result
