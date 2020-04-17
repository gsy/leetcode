class Solution:
    def canJump(self, nums):
        length = len(nums)
        if length <= 1:
            return True

        minimum = 1
        for i in range(length - 2, -1, -1):
            steps = nums[i]
            if steps >= minimum:
                minimum = 1
                result = True
            else:
                minimum = minimum + 1
                result = False

        return result
