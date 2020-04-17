# -*- coding: utf-8 -*-

from burst_balloons import Solution

if __name__ == '__main__':
    s = Solution()
    result = s.maxCoins([3, 1, 5, 8])
    print(result)
    assert result == 167

    result = s.maxCoins([10, 2, 3, 1, 1, 1000])
    print(result)
    assert result == 45060

    result = s.maxCoins([9, 76, 64, 21])
    print(result)
    assert result == 116718
