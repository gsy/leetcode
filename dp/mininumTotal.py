class Solution:
    def minimumTotal(self, triangle):
        m = len(triangle)
        n = len(triangle[-1])

        A = [[0] * n for i in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(i, -1, -1):
                if i == m-1:
                    A[i][j] = triangle[i][j]
                else:
                    A[i][j] = triangle[i][j] + min(A[i+1][j+1], A[i+1][j])

        return A[0][0]
