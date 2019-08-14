# -*- coding: utf-8 -*-

class Solution:
    def maximalSquare(self, matrix):
        rows, columns = len(matrix), 0
        if rows > 0:
            columns = len(matrix[0])

        current, result = 0, 0
        # 包含 i,j 点的正方形
        # a[i][j] = i * j if a[i-1][j-1] == (i - 1) * (j - 1) and a[i][c] == 1 and a[r][j] == 1
        areas = []
        for i in range(rows):
            row = []
            for j in range(columns):
                if matrix[i][j] == 1:
                    row.append(1)
                else:
                    row.append(0)
            areas.append(row)

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    current = 0
                else:
                    # 自身是不是正方形
                    # 边长更小的是不是正方形


                areas[i][j] = current
                if current > result:
                    result = current
        return result
