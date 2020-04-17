# -*- coding: utf-8 -*-


class Solution:
    def sortedSquares(self, ls):
        return sorted([item * item for item in ls])


if __name__ == '__main__':
    s = Solution()
    r = s.sortedSquares([-4,-1,0,3,10])
    assert r == [0,1,9,16,100]

    r = s.sortedSquares([-7,-3,2,3,11])
    assert r == [4,9,9,49,121]
