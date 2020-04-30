# 1. 所有的 num 除以一个数，累加和不能大于 threshold
# 2. 这个除数必须小
# 3. 累加和大了，说明什么？除数要变大


class Solution:
    def check(self, nums, divisor, threshold):
        acc = 0
        for num in nums:
            floor = 0 if (num % divisor == 0) else 1
            acc = acc + (num // divisor + floor)
            if acc > threshold:
                return 1
        if acc == threshold:
            return 0

        return -1

    def smallestDivisor(self, nums, threshold):
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            acc = self.check(nums, mid, threshold)
            # 累加和大
            if acc > 0:
                left = mid + 1
            else:
                right = mid

        return left
