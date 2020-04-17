# -*- coding: utf-8 -*-

from broken_calculator import Solution


if __name__ == '__main__':
    s = Solution()
    result = s.brokenCalc(5, 8)
    print(result)
    assert result == 2

    result = s.brokenCalc(3, 10)
    print(result)
    assert result == 3

    result = s.brokenCalc(1024, 1)
    print(result)
    assert result == 1023

    result = s.brokenCalc(363, 811)
    print(result)
    assert result == 163
