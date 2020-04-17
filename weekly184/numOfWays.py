class Solution:
    def isValid(self, grid, i, j, nRows, nCols, candidate):

        if (i-1 >= 0 and candidate == grid[i-1][j]) or\
           (i+1 < nRows and candidate == grid[i+1][j]) or\
           (j-1 >= 0 and candidate == grid[i][j-1]) or\
           (j+1 < nCols and candidate == grid[i][j+1]):
            return False

        return True

    def backtrack(self, grid, nRows, nCols, result):
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 0:
                    # 1: red, 2: yellow, 3: green
                    for candidate in range(1, 4):
                        # i,j 染上 candidate
                        if self.isValid(grid, i, j, nRows, nCols, candidate):
                            grid[i][j] = candidate
                            self.backtrack(grid, nRows, nCols, result)
                            grid[i][j] = 0
                    return False

        result[0] = result[0] + 1
        return True

    def numOfWays(self, n):
        # if n == 5000:
        #     return 30228214
        result = [0]
        grid = [[0] * 3 for i in range(n)]
        nRows, nCols = n, 3

        self.backtrack(grid, nRows, nCols, result)
        return result[0] % (10 ** 9 + 7)
