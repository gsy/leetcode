class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        A = [[0] * n] * m

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    A[i][j] = grid[i][j]
                elif i == 0:
                    A[i][j] = A[i][j-1] + grid[i][j]
                elif j == 0:
                    A[i][j] = A[i-1][j] + grid[i][j]
                else:
                    A[i][j] = min(A[i-1][j], A[i][j-1]) + grid[i][j]
        return A[m-1][n-1]
