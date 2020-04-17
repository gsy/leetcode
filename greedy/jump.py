class Solution:
    def jump(self, nums):
        length = len(nums)

        # 中继点
        candidates = []
        weight = []
        result = 0
        N = 1
        steps = []
        for i in range(length-2, -1, -1):
            if nums[i] >= N:
                candidates.append(N)
                # 记下这个点的最少的步数
                steps = None

                # 这个都是步数啊，有啥用？
                for c in candidates:



                weight.append(steps)
                N = 1
            else:
                N = N + 1
        return result
