# -*- coding: utf-8 -*-


class Solution(object):
    def maxArea(self, height):
        length = len(height)
        if length == 0:
            return 0

        matrix = [[0] * length] * length
        result = 0
        for i in range(length):
            for j in range(i + 2, length):
                if (height[i] > height[i+1]):
                    matrix[i][j] = matrix[i+1][j] * (j - i)
                else:
                    matrix[i][j] = matrix[i+1][j-1]
        return matrix[i]



if __name__ == '__main__':
    s = Solution()
    r = s.maxArea([1, 4, 7, 8])
    assert r == 8
    r = s.maxArea([])
    assert r == 0
    r = s.maxArea([1])
    assert r == 0
    r = s.maxArea([1, 10])
    assert r == 0
