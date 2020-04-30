from functools import cmp_to_key


class Solution:
    def compare(self, item1, item2):
        if item1[1] > item2[1]:
            return 1
        elif item1[1] < item2[1]:
            return -1
        else:
            if item1[0] < item2[0]:
                return -1
            elif item1[0] > item2[0]:
                return 1
        return 0

    def kWeakestRows(self, mat, k):
        nRows = len(mat)
        nCols = len(mat[0])

        # 维护一个最小堆，使用 count 去比较，最后取出来的是 key
        power = {}
        for i in range(nRows):
            count = 0
            for j in range(nCols):
                if mat[i][j] == 0:
                    break
                else:
                    count = count + 1
            power[i] = count

        ls = sorted(power.items(), key=cmp_to_key(self.compare))
        result = []
        for i in range(k):
            result.append(ls[i][0])
        return result
