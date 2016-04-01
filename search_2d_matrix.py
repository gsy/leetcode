__author__ = 'guang'

class Solution(object):
    def one_d_to_two_d_index(self, index, columns):
        """
        >>> s = Solution()
        >>> s.one_d_to_two_d_index(0, 3, 4)
        (0, 0)
        >>> s.one_d_to_two_d_index(11, 3, 4)
        (2, 3)
        >>> s.one_d_to_two_d_index(5, 3, 4)
        (1, 1)
        >>> s.one_d_to_two_d_index(4, 3, 4)
        (1, 0)
        >>> s.one_d_to_two_d_index(8, 3, 4)
        (2, 0)
        >>> s.one_d_to_two_d_index(7, 3, 4)
        (1, 3)
        """
        row = index / columns
        column = index - row * columns
        return row, column

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        >>> s = Solution()
        >>> matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        >>> s.searchMatrix(matrix, 3)
        True
        >>> s.searchMatrix(matrix, 16)
        True
        >>> s.searchMatrix(matrix, 1)
        True
        >>> s.searchMatrix(matrix, 50)
        True
        >>> s.searchMatrix(matrix, 22)
        False
        >>> s.searchMatrix([[1], [2]], 1)
        True
        >>> s.searchMatrix([[1], [2]], 3)
        False
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows = len(matrix)
        columns = len(matrix[0])
        left, right = 0, rows * columns - 1
        while left <= right:
            middle = (left + right) / 2
            row, column = self.one_d_to_two_d_index(middle, columns)
            value = matrix[row][column]
            if value == target:
                return True
            elif value < target:
                left = middle + 1
            else:
                right = middle - 1

        return False





