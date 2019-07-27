# -*- coding: utf-8 -*-


class Solution:
    def safe_get(self, matrix, rows, columns, i, j):
        if (0 <= i < rows) and (0 <= j < columns):
            return matrix[i][j]
        return 0

    def common_length(self, word1, length1, word2, length2):
        # 找到两个字符串的最大公共子序列
        result = 0
        matrix = [[0] * length2 for row in range(length1)]

        for i in range(length1):
            for j in range(length2):
                if word1[i] == word2[j]:
                    matrix[i][j] = self.safe_get(matrix, length1, length2, i-1, j-1) + 1
                else:
                    sub1 = self.safe_get(matrix, length1, length2, i-1, j)
                    sub2 = self.safe_get(matrix, length1, length2, i, j-1)
                    matrix[i][j] = max(sub1, sub2)
                if matrix[i][j] > result:
                    result = matrix[i][j]
        print(matrix, result)
        return result

    def minDistance(self, word1, word2):
        length1, length2 = len(word1), len(word2)
        return length1 + length2 - 2 * self.common_length(word1, length1, word2, length2)


if __name__ == '__main__':
    s = Solution()
    r = s.minDistance("sea", "eat")
    print(r)
    assert r == 2

    r = s.minDistance("hello", "world")
    print(r)
    assert r == 8

    r = s.minDistance("hello", "worldo")
    print(r)
    assert r == 7

    r = s.minDistance("a", "a")
    print(r)
    assert r == 0

    # r = s.minDistance("", "")
    # print(r)
    # assert r == 0

    r = s.minDistance("a", "ab")
    print(r)
    assert r == 1

    r = s.minDistance("zoologicoarchaeologist", "zoogeologist")
    print(r)
    assert r == 10
