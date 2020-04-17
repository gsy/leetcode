# -*- coding: utf-8 -*-


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        A = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    A[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        A[i][j] = 1
                    elif i == 0:
                        A[i][j] = A[i][j-1]
                    elif j == 0:
                        A[i][j] = A[i-1][j]
                    else:
                        A[i][j] = A[i-1][j] + A[i][j-1]

        return A[m-1][n-1]
