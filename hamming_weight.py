# -*- coding: utf-8 -*-


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count('1')


if __name__ == '__main__':
    s = Solution()
    r = s.hammingWeight(00000000000000000000000000001011)
    print(r)
    assert r == 3

    # r = s.hammingWeight(00000000000000000000000010000000)
    # assert r == 1

    r = s.hammingWeight(11111111111111111111111111111101)
    print(r)
    assert r == 31
