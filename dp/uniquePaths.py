# -*- coding: utf-8 -*-


class Solution:
    def uniquePaths(self, m, n):
        if m <= 1 or n <= 1:
            return 1

        A = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    A[i][j] = 0
                elif (i == 0 or j == 0):
                    A[i][j] = 1
                else:
                    A[i][j] = A[i-1][j] + A[i][j-1]
        return A[m-1][n-1]
