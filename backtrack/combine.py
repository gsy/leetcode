class Solution:
    def backtrack(self, nums, k, start, end, path, result):
        print(start, end, path)
        if len(path) == k:
            print(path)
            result.append([item for item in path])
            return

        for i in range(start, end):
            # 对于这1轮来说，candidates 是 start+1 到 end 的数
            path.append(nums[i])
            self.backtrack(nums, k, start+1, end, path, result)
            path.pop(-1)

        return

    def combine(self, n, k):
        nums = [i for i in range(1, n+1)]
        result = []
        self.backtrack(nums, k, 0, n, [], result)
        return result
