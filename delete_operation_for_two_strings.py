# -*- coding: utf-8 -*-


class Solution:
    def common_length(self, word1, length1, word2, length2):
        # 找到两个字符串的最大公共子序列
        # matrix 的 i， j 下标分别是两个字符串的最后字符下标
        matrix = [[0] * length2] * length2

        result = 0
        for step in range(1, length2):
            for start in range(0, length2 - step):
                i, j = start, start + step
                print(i, j)

                # 这里存的是距离
                matrix[i][j] = max(
                    matrix[i-1][j] + (1 if word1[i] == word2[i] else 0),
                    matrix[i][j-1] + (1 if word1[j] == word2[j] else 0),
                )
                if matrix[i][j] > result:
                    result = matrix[i][j]
        print(matrix)
        return result

    def minDistance(self, word1, word2):
        length1, length2 = len(word1), len(word2)
        return length1 + length2 - self.common_length(word1, length1, word2, length2)


if __name__ == '__main__':
    s = Solution()
    r = s.minDistance("sea", "eat")
    print(r)
    assert r == 2
