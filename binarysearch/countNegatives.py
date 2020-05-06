class Solution:
    def countNegatives(self, grid):
        nRows = len(grid)
        nCols = len(grid[0])

        count = 0
        for i in range(nRows):
            ls = grid[i]
            left, right = 0, nCols - 1

            found = False
            while left <= right:
                mid = (left + right) // 2
                if ls[mid] >= 0:
                    left = mid + 1
                else:
                    found = True
                    right = mid - 1

            # print("i", i, "left", left, "found", found)
            if found:
                count += (nCols - left)
        return count
