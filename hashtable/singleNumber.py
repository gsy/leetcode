class Solution:
    def singleNumber(self, nums):
        result = None
        for num in nums:
            if result is None:
                result = num
            else:
                result = result ^ num
        return result
