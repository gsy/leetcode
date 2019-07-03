# -*- coding: utf-8 -*-

from climbing_stairs import Solution


if __name__ == '__main__':
    s = Solution()
    result = s.climbStairs(3)
    assert result == 3

    result = s.climbStairs(4)
    assert result == 5

    result = s.climbStairs(5)
    assert result == 8
