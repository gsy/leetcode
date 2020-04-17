class Solution:
    def permute(self, nums):
        length = len(nums)
        if length == 0:
            return []

        if length == 1:
            return [nums]

        result = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            tmp = [item for item in nums]
            tmp.pop(i)

            sub = self.permute(tmp)
            for ls in sub:
                ls.append(num)
                result.append(ls)

        return result

    def permuteUnique(self, nums):
        length = len(nums)
        if length == 0:
            return []

        nums = sorted(nums)
        result = self.permute(nums)
        return result
