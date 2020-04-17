class Solution:
    def toInt(self, arr):
        base = 1
        result = 0
        for i in range(len(arr)-1, -1, -1):
            result = result + base * arr[i]
            base = base * 2
        return result

    def matrixScore(self, A):
        nRows = len(A)
        nCols = len(A[0])

        better = True
        while better:
            # 总是先翻转行再翻转列？
            better = False
            for i in range(nRows):
                # 翻转行或者列，如果翻转行
                if A[i][0] == 0:
                    better = True
                    for j in range(nCols):
                        print(i, j, A[i][j])
                        if A[i][j] == 0:
                            A[i][j] = 1
                        else:
                            A[i][j] = 0
            # print("step1", A)

            for j in range(nCols):
                count = 0
                for i in range(nRows):
                    if A[i][j] == 0:
                        count = count + 1

                if count > nRows // 2:
                    better = True
                    for i in range(nRows):
                        if A[i][j] == 0:
                            A[i][j] = 1
                        else:
                            A[i][j] = 0
            # print("step2", A)

        result = 0
        for i in range(nRows):
            result += self.toInt(A[i])
        return result
