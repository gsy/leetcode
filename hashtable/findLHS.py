class Solution:
    def findLHS(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        keys = count.keys()
        keys = sorted(keys)

        prev = None
        result = 0
        length = 0
        for key in keys:
            value = count[key]
            if prev is not None and key - prev == 1:
                length = value + count[prev]
                if length >= result:
                    result = length
            prev = key

        return result
