
class Solution:
    def take_three_out_of(self, nums):
        # 怎样可以拿出全部的 permutation?
        for i, x in enumerate(nums):
            set1 = [nums[index] for index in range(len(nums)) if index != i]
            for j, y in enumerate(set1):
                set2 = [set1[index] for index in range(len(set1)) if index != j]
                for z in set2:
                    yield [x, y, z]

    def threeSum(self, nums):
        if len(nums) == 0:
            return []

        negative, positive, zero = [], [], []
        for item in nums:
            if item > 0:
                positive.append(item)
            elif item < 0:
                negative.append(item)
            else:
                zero.append(item)

        if len(negative) == 0 and len(positive) == 0 and len(zero) >= 3:
            return [[0, 0, 0]]
        elif len(negative) == 0 or len(positive) == 0:
            return []

        result = []
        for c in set(nums):
            z = int(-1 * c)
            if z == 0:
                a = self.take_one_out_of(positive)
                b = self.take_one_out_of(negative)
                if a + b == z:
                    result.append([a, b, c])
            elif z > 0:
                a = self.take_one_out_of(positive)
                b = self.take_one_out_of(nums)
                if a + b == z:
                    result.append([a, b, c])
            elif z < 0:
