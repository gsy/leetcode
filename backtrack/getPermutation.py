class Solution:
    def backtrack(self, nums, count, k, result):
        if len(nums) == 1:
            result.append(str(nums[0]))
            count[0] = count[0] + 1
            print(result, count[0])
            if count[0] == k:
                return True
            else:
                result.pop(-1)
                return False

        if count[0] == k:
            return True

        for i, num in enumerate(nums):
            tmp = [n for n in nums]
            tmp.pop(i)

            result.append(str(num))
            if len(tmp) > 0:
                done = self.backtrack(tmp, count, k, result)
                if done:
                    return True
                else:
                    result.pop(-1)
            else:
                result.pop(-1)
        return False

    def getPermutation(self, n, k):
        result = []
        nums = [i for i in range(1, n+1)]
        count = [0]
        self.backtrack(nums, count, k, result)
        return ''.join(result)
