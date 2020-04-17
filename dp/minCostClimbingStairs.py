class Solution:
    def minCostClimbingStairs(self, cost):
        length = len(cost)
        A = [0] * length

        for i in range(length):
            if i <= 1:
                A[i] = cost[i]
            else:
                A[i] = min(A[i-1], A[i-2]) + cost[i]

        return min(A[length-1], A[length-2])
