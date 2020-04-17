# -*- coding: utf-8 -*-


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        A = [[0] * len2 for i in range(len1)]
        if len1 == 0 and len2 == 0:
            return 0
        elif len1 == 0:
            return len2
        elif len2 == 0:
            return len1

        for i in range(len1):
            for j in range(len2):
                x = word1[i]
                y = word2[j]

                if x == y:
                    if i == 0 and j == 0:
                        A[i][j] = 0
                    elif i == 0:
                        A[i][j] = j
                    elif j == 0:
                        A[i][j] = i
                    else:
                        A[i][j] = A[i-1][j-1]
                else:
                    if i == 0 and j == 0:
                        A[i][j] = 1
                    elif i == 0:
                        # 添加
                        A[i][j] = min(A[i][j-1]+1, j + 1)
                    elif j == 0:
                        # 删除
                        A[i][j] = min(A[i-1][j] + 1, i + 1)
                    else:
                        A[i][j] = min(A[i-1][j-1] + 1, A[i-1][j] + 1, A[i][j-1]+1)

        print(A)
        return A[len1-1][len2-1]
