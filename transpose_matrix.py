# -*- coding: utf-8 -*-


class Solution:
    def transpose(self, a):
        rows = len(a)
        if rows == 0:
            return []

        columns = len(a[0])
        result = [[0] * rows for column in range(columns)]
        for column in range(columns):
            for row in range(rows):
                result[column][row] = a[row][column]
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(r)

    r = s.transpose([[1, 2, 3], [4, 5, 6]])
    print(r)
