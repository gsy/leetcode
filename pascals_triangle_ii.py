# -*- coding: utf-8 -*-

class Solution:
    def getRow(self, n):
        # 第一个数肯定是1，第二个数是n, 第3个数是
        #    1
        #   1 1
        #   1 2 1
        #   1 3 3 1
        #   1 4 6 4 1 6: 1 + 2 + 3
        #   1 5 10 10 5 1, 10: 1 + 2 + 3 + 4
        # 中间点是 sum(range(1, int(n+1)/2)
        result = [1]
        for i in range(n+1):
            for j in range(int(i+1)/2):
                if j == 0 or j == i:
                    result.append(1)
                elif j == 1:
                    result.append(i + )

        return current


if __name__ == "__main__":
    s = Solution()
    r = s.getRow(3)
    print(r)
    assert r == [1, 3, 3, 1]

    r = s.getRow(2)
    print(r)
    assert r == [1, 2, 1]

    r = s.getRow(1)
    print(r)
    assert r == [1, 1]
