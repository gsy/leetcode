# -*- coding: utf-8 -*-


class Solution:
    def value_of(self, index, matrix, rows, columns):
        row = int(index / columns)
        column = index % columns
        return matrix[row][column]

    def searchMatrix(self, matrix, target):
        # 折行递增
        rows = len(matrix)
        if rows == 0:
            return False
        columns = len(matrix[0])
        if columns == 0:
            return False

        length = rows * columns
        left, right = 0, length - 1
        while left <= right:
            middle = int((left + right) / 2)
            value = self.value_of(middle, matrix, rows, columns)
            # print("middel {}, value {}".format(middle, value))
            if value == target:
                return True
            elif value > target:
                right = middle - 1
            else:
                left = middle + 1
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    r = s.searchMatrix(matrix, 3)
    assert r is True

    r = s.searchMatrix(matrix, 16)
    assert r is True

    r = s.searchMatrix(matrix, 1)
    assert r is True

    r = s.searchMatrix(matrix, 50)
    assert r is True

    r = s.searchMatrix(matrix, 52)
    assert r is False

    r = s.searchMatrix(matrix, 2)
    assert r is False

    matrix = [
        [1,   3],
        [10, 11]
    ]
    r = s.searchMatrix(matrix, 3)
    assert r is True
