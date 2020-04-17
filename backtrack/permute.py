class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        result = []
        for i, num in enumerate(nums):
            tmp = [item for item in nums]
            tmp.pop(i)

            sub = self.permute(tmp)

            for ls in sub:
                ls.append(num)
                result.append(ls)

        return result
