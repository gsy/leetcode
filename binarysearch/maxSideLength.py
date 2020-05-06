class Solution:
    def sumAll(self, A, mat, left, right, steps):
        x1, y1 = left
        x2, y2 = right

        if x1 == 0 and y1 == 0:
            return A[x2][y2]

        if x1 >= 1 and y1 >= 1:
            return A[x2][y2] - A[x1-1][y2] - A[x2][y1-1] + A[x1-1][y1-1]
        elif x1 >= 1:
            return A[x2][y2] - A[x1-1][y2]
        elif y1 >= 1:
            return A[x2][y2] - A[x2][y1-1]
        else:
            return A[x2][y2]

    def maxSideLength(self, mat, threshold):
        nRows = len(mat)
        nCols = len(mat[0])
        A = [[0 for j in range(nCols)] for i in range(nRows)]

        for i in range(nRows):
            for j in range(nCols):
                if i - 1 >= 0 and j - 1 >= 0:
                    A[i][j] = A[i-1][j] + A[i][j-1] - A[i-1][j-1] + mat[i][j]
                elif i - 1 >= 0:
                    A[i][j] = A[i-1][j] + mat[i][j]
                elif j - 1 >= 0:
                    A[i][j] = A[i][j-1] + mat[i][j]
                else:
                    A[i][j] = mat[i][j]

        result = 0
        for i in range(nRows):
            for j in range(nCols):
                left = (i, j)
                steps = 1
                while (i + steps) < nRows and (j + steps) < nCols:
                    right = (i+steps, j+steps)
                    steps = steps + 1
                    tmp = self.sumAll(A, mat, left, right, steps)
                    if tmp <= threshold:
                        if steps > result:
                            # print("steps", steps, "length", tmp, "left", left, "right", right)
                            result = steps
                    else:
                        break

        return result
