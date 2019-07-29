# -*- coding: utf-8 -*-


class Solution:
    def safe_get(self, grid, rows, columns, row, column):
        if 0 <= row < rows and 0 <= column < columns:
            return grid[row][column]

        return 0

    def islandPerimeter(self, grid):
        # 1 有4条边，所以周长等于边数 * 4, 如果有边跟其他边重复，算两边也是没有问题的

        edges, duplicate = 0, 0
        rows, columns = len(grid), len(grid[0])

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    edges = edges + 1
                    # 只检查上面和左边
                    if self.safe_get(grid, rows, columns, row-1, column) == 1:
                        duplicate = duplicate + 2
                    if self.safe_get(grid, rows, columns, row, column-1) == 1:
                        duplicate = duplicate + 2

        return edges * 4 - duplicate


if __name__ == '__main__':
    s = Solution()
    r = s.islandPerimeter([[0, 1, 0, 0],  [1, 1, 1, 0],  [0, 1, 0, 0],  [1, 1, 0, 0]])
    print(r)
    assert r == 16
