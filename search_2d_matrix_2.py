__author__ = 'guang'

class Solution(object):
    def search(self, a, target):
        length = len(a)
        if length < 1:
            return False

        left, right = 0, length - 1
        while left <= right:
            index = (left + right) / 2
            middle = a[index]
            if middle == target:
                return True
            elif middle < target:
                left = middle + 1
            else:
                right = middle - 1

        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        >>> s = Solution()
        >>> matrix = [[1, 3, 4, 7, 10]]
        >>> s.searchMatrix(matrix, 1)
        True
        >>> s.searchMatrix(matrix, 3)
        True
        >>> s.searchMatrix(matrix, 10)
        True
        >>> s.searchMatrix(matrix, 7)
        True
        >>> s.searchMatrix(matrix, 6)
        False
        >>> matrix = [[1], [3], [4], [7], [10]]
        >>> s.searchMatrix(matrix, 1)
        True
        >>> s.searchMatrix(matrix, 3)
        True
        >>> s.searchMatrix(matrix, 10)
        True
        >>> s.searchMatrix(matrix, 7)
        True
        >>> s.searchMatrix(matrix, 6)
        False
        >>> matrix = [[1, 4, 7, 11, 15],[2, 5, 8, 12, 19],[3, 6, 9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]]
        >>> s.searchMatrix(matrix, 1)
        True
        >>> s.searchMatrix(matrix, 30)
        True
        >>> s.searchMatrix(matrix, 28)
        False
        >>> s.searchMatrix(matrix, 26)
        True
        >>> s.searchMatrix(matrix, 24)
        True
        >>> matrix = [[1, 4, 7, 11],[2, 5, 8, 12],[3, 6, 9, 16],[10, 13, 14, 17],[18, 21, 23, 26]]
        >>> s.searchMatrix(matrix, 1)
        True
        >>> s.searchMatrix(matrix, 4)
        True
        >>> s.searchMatrix(matrix, 3)
        True
        >>> s.searchMatrix(matrix, 5)
        True
        >>> s.searchMatrix(matrix, 30)
        False
        >>> s.searchMatrix(matrix, 28)
        False
        >>> s.searchMatrix(matrix, 26)
        True
        >>> s.searchMatrix(matrix, 24)
        False
        >>> s.searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 15)
        True
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows = len(matrix)
        columns = len(matrix[0])

        bottom, top = rows-1, 0
        while top <= bottom:
            middle_x = (bottom + top) / 2
            if self.search(matrix[middle_x], target):
                return True
            elif target > matrix[middle_x][columns-1]:
                left = middle_x + 1
            elif target <






