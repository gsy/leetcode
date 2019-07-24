# -*- coding: utf-8 -*-
# https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries/


class Solution:
    def sumEvenAfterQueries(self, ls, queries):
        result = []
        even_sum = sum(item for item in ls if item % 2 == 0)
        for val, index in queries:
            if ls[index] % 2 == 0:
                # 原来是偶数，那么得减掉原来的值
                even_sum = even_sum - ls[index]
            current = ls[index] + val
            if current % 2 == 0:
                even_sum = even_sum + current
            ls[index] = current
            result.append(even_sum)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.sumEvenAfterQueries(ls=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]])
    print(r)
    assert r == [8, 6, 2, 4]
